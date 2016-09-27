
####################################################################
# File: audit_osm_data.py
#
# Description: This code will audit city data collected in the
# format XML OSM. The intention of this code is to analyze a city
# dataset and recognize issues and inconsistencies with the
# supplied dataset.
####################################################################

import xml.etree.cElementTree as ET
import csv
import codecs
import re
import pprint
from collections import defaultdict

# ================================================== #
# Input File
# ================================================== #
OSM_FILE = 'denver-boulder_colorado_small.osm'
#OSM_FILE = 'denver-boulder_colorado.osm'

# ================================================== #
# Output Files
# ================================================== #
NODES_PATH     = "nodes.csv"
NODE_TAGS_PATH = "nodes_tags.csv"
WAYS_PATH      = "ways.csv"
WAY_NODES_PATH = "ways_nodes.csv"
WAY_TAGS_PATH  = "ways_tags.csv"

# ================================================== #
# Output File Formatting
# ================================================== #
NODE_FIELDS      = ['id', 'lat', 'lon', 'user', 'uid', 'version', 'changeset', 'timestamp']
NODE_TAGS_FIELDS = ['id', 'key', 'value', 'type']
WAY_FIELDS       = ['id', 'user', 'uid', 'version', 'changeset', 'timestamp']
WAY_TAGS_FIELDS  = ['id', 'key', 'value', 'type']
WAY_NODES_FIELDS = ['id', 'node_id', 'position']

# ================================================== #
# Regex forms
# ================================================== #
street_type_re   = re.compile(r'\b([A-Z]?[a-z]+).?$|\b(\d+).?$', re.IGNORECASE)
lower_re         = re.compile(r'^([a-z]|_)*$')
lower_colon_re   = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problem_chars_re = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')

# ================================================== #
# Expected street type names
# ================================================== #
expected = ["Street",
            "Avenue",
            "Boulevard",
            "Drive",
            "Court",
            "Place",
            "Square",
            "Lane",
            "Road",
            "Trail",
            "Parkway",
            "Commons",
            "Way",
            "Circle"]

# ================================================== #
# Mapping for correcting street type names
# ================================================== #
MAPPING = {"St":      "Street",
           "Strret":  "Street",
           "Street ": "Street",
           "st":      "Street",
           "ST.":     "Street",
           "Ave":     "Avenue",
           "ave.":    "Avenue",
           "Ave.":    "Avenue",
           "Av":      "Avenue",
           "avenue":  "Avenue",
           "Rd.":     "Road",
           "Rd":      "Road",
           "rd":      "Road",
           "Raod":    "Road",
           "Pkwy":    "Parkway",
           "Pky":     "Parkway",
           "ct":      "Court",
           "Dr":      "Drive",
           "dr":      "Drive",
           "trail":   "Trail",
           "Pl":      "Place",
           "Ct":      "Court",
           "Blvd":    "Boulevard",
           "ste.":    "Suite",
           "Ste":     "Suite",
           "ste":     "Suite"}

# ================================================== #
# Function to audit an OSM file and check for
# unexpected zip codes
# ================================================== #
def audit_zip_codes(osmfile):
    osm_file = open(osmfile, "r")
    unexp_zip_codes = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_zip_code(tag):
                    unexp_zip_codes = check_zip_code(unexp_zip_codes, tag.attrib['v'])
    osm_file.close()
    return unexp_zip_codes


# ================================================== #
# Function to audit an OSM file and count the number
# of tags by type
# ================================================== #
def audit_tags(filename):
    tags = {}
    for event, elem in ET.iterparse(filename):
        if elem.tag in tags:
            tags[elem.tag] += 1
        else:
            tags[elem.tag] = 1
    return tags


# ================================================== #
# Function to audit an OSM file and count the number
# of tags that contain potential problem characters
# ================================================== #
def audit_problem_tags(filename):
    keys = {"lower":         0,
            "lower_colon":   0,
            "problem_chars": 0,
            "other":         0}
    for _, element in ET.iterparse(filename):
        keys = categorize_key_type(element, keys)
    return keys


# ================================================== #
# Function to audit an OSM file and count the number
# of unique users that have contributed to the data
# ================================================== #
def audit_users(filename):
    users = set()
    for _, element in ET.iterparse(filename):

        if element.tag == "node":
            for tag in element.iter("node"):
                if tag.attrib['user'] not in users:
                    users.add(tag.attrib['user'])
        if element.tag == "relation":
            for tag in element.iter("relation"):
                if tag.attrib['user'] not in users:
                    users.add(tag.attrib['user'])
        if element.tag == "way":
            for tag in element.iter("way"):
                if tag.attrib['user'] not in users:
                    users.add(tag.attrib['user'])
    return users


# ================================================== #
# Function to audit an OSM file and find all street
# names that do not match an expected value
# ================================================== #
def audit_unexpected_streets(osmfile):
    osm_file = open(osmfile, "r")
    unexp_street_types = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    address = tag.attrib['v']
                    unexp_street_types = check_street_unexp(unexp_street_types, address)
                    fix_street_name(address, MAPPING)
    osm_file.close()
    return unexp_street_types


# ================================================== #
# Function to audit an OSM file and count the number
# of each street type
# ================================================== #
def audit_street_types(osmfile):
    osm_file = open(osmfile, "r")
    street_types_count = defaultdict(set)
    initialize_street_types_count(street_types_count)
    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    street_types_count = check_street_exp(street_types_count, tag.attrib['v'])
    osm_file.close()
    return street_types_count


# ================================================== #
# Helper Function to categorize a tag type
# ================================================== #
def categorize_key_type(element, keys):

    if element.tag == "tag":
        for tag in element.iter("tag"):

            # "lower", for tags that contain only
            # lowercase letters and are valid
            if lower_re.search(tag.attrib['k']):
                keys['lower'] += 1

            # "lower_colon", for otherwise valid
            # tags with a colon in their names
            elif lower_colon_re.search(tag.attrib['k']):
                keys['lower_colon'] += 1

            # "problem_chars", for tags with
            # problematic characters
            elif problem_chars_re.search(tag.attrib['k']):
                keys['problem_chars'] += 1

            # "other", for other tags that do not fall
            # into the other three categories
            else:
                keys['other'] += 1
    return keys


# ================================================== #
# Helper Function to determine if a zip code has an
# unexpected value or format
# ================================================== #
def check_zip_code(unexp_zip_codes, zip_code):

    # Check if zip code is exactly 5 digits
    if len(zip_code) != 5:
        if zip_code in unexp_zip_codes:
            unexp_zip_codes[zip_code] += 1
        else:
            unexp_zip_codes[zip_code] = 1

    # check if zip code is in the correct range
    else:
        if int(zip_code[0]) != 8 and int(zip_code[1]) != 0:
            if zip_code in unexp_zip_codes:
                unexp_zip_codes[zip_code] += 1
            else:
                unexp_zip_codes[zip_code] = 1

    return unexp_zip_codes


# ================================================== #
# Helper Function to determine if a street name
# has an expected name
# ================================================== #
def check_street_unexp(unexp_street_types, street_name):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected:
            unexp_street_types[street_type].add(street_name)
    return unexp_street_types


# ================================================== #
# Helper Function to determine if a street name has
# an expected format and increment a list of all
# street name types
# ================================================== #
def check_street_exp(exp_street_types, street_name):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type in expected:
            exp_street_types[street_type] += 1
    return exp_street_types


# ================================================== #
# Helper Function to check if zip code is valid
# ================================================== #
def is_zip_valid(zip_code):

    # Check if zip code is exactly 5 digits
    if len(zip_code) != 5:
        return False

    # check if zip code is in the correct range
    elif int(zip_code[0]) != 8 and int(zip_code[1]) != 0:
        return False

    # Passes test - valid
    else:
        return True

# ================================================== #
# Helper Function to check if tag is an address tag
# ================================================== #
def is_street_name(tag):

    if (tag == "addr:street"):
        return True
    else:
        return False

# ================================================== #
# Helper Function to check if tag is a zip code
# Only look for zip_left from tiger data (don't
# want 2 copies of the zip code element
# ================================================== #
def is_zip_code(elem):
    if (elem.attrib['k'] == "addr:postcode" or
        elem.attrib['k'] == "tiger:zip_left" or
        elem.attrib['k'] == "tiger:zip_right"):
        return True
    else:
        return False


# ================================================== #
# Helper Function to initialize the dictionary that
# stores the street type counts
# ================================================== #
def initialize_street_types_count(street_types_count):
    for street_type in expected:
        street_types_count[street_type] = 0


# ================================================== #
# Helper Function to update a bad street name based
# on a defined mapping
# ================================================== #
def fix_street_name(address, mapping):
    words = address.split()
    for w in range(len(words)):
        if words[w] in mapping:
            # Don't update 'Apartment E' to 'Apartment East'
            if words[w-1].lower() in [ 'apartment', 'apt', 'building', 'suite', 'ste.', 'ste']:
                continue
            else:
                words[w] = mapping[words[w]]
                address = " ".join(words)
    return address


# ================================================== #
# Helper Function to grab an element from the OSM
# ================================================== #
def get_element(osm_file, tags=('node', 'way', 'relation')):
    """Yield element if it is the right type of tag"""

    context = ET.iterparse(osm_file, events=('start', 'end'))
    _, root = next(context)
    for event, elem in context:
        if event == 'end' and elem.tag in tags:
            yield elem
            root.clear()

# ================================================== #
# Helper Function to write to csv files
# ================================================== #
class UnicodeDictWriter(csv.DictWriter, object):
    """Extend csv.DictWriter to handle Unicode input"""

    def writerow(self, row):
        super(UnicodeDictWriter, self).writerow({
                                                    k: (v.encode('utf-8') if isinstance(v, unicode) else v) for
                                                    k, v in
                                                    row.iteritems()
                                                    })

    def writerows(self, rows):
        for row in rows:
            self.writerow(row)


# ================================================== #
# Function to audit and find issues with the data
# ================================================== #
def audit():

    '''
    '''

    # Count the number of unique tags within the XML file
    tags = audit_tags(OSM_FILE)
    pprint.pprint(tags)

    '''
    # Count the number of potential problem tags
    keys = audit_problem_tags(OSM_FILE)
    pprint.pprint(keys)
    '''

    '''
    # Count the number of unique users that have contributed
    users = audit_users(OSM_FILE)
    pprint.pprint(len(users))
    '''

    '''
    # Audit the street names and formatting
    unexp_street_types = audit_unexpected_streets(OSM_FILE)
    # pprint.pprint(dict(unexp_street_types))
    '''

    '''
    # Count the number of street types
    street_types_count = audit_street_types(OSM_FILE)
    pprint.pprint(dict(street_types_count))
    '''

    '''
    # Audit the zip codes of elements
    unexp_zip_codes = audit_zip_codes(OSM_FILE)
    pprint.pprint(dict(unexp_zip_codes))
    '''


# ================================================== #
# Main()
# ================================================== #
if __name__ == "__main__":
    print("Running...")
    audit()
