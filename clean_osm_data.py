####################################################################
# File: clean_osm_data.py
#
# Description: This code will audit city data collected in the
# format XML OSM. The intention of this code is to analyze a city
# dataset and recognize issues and inconsistencies with the
# supplied dataset.
####################################################################

import xml.etree.cElementTree as ET
import csv
import codecs
from collections import defaultdict

# ================================================== #
# Input File
# ================================================== #
OSM_FILE = 'denver-boulder_colorado_small.osm'
# OSM_FILE = 'denver-boulder_colorado.osm'

# ================================================== #
# Output Files
# ================================================== #
NODES_PATH     = "nodes.csv"
NODE_TAGS_PATH = "node_tags.csv"
WAYS_PATH      = "ways.csv"
WAY_NODES_PATH = "way_nodes.csv"
WAY_TAGS_PATH  = "way_tags.csv"

# ================================================== #
# Output File Formatting
# ================================================== #
NODE_FIELDS      = ['id', 'lat', 'lon', 'user', 'uid', 'version', 'changeset', 'timestamp']
NODE_TAGS_FIELDS = ['id', 'key', 'value', 'type']
WAY_FIELDS       = ['id', 'user', 'uid', 'version', 'changeset', 'timestamp']
WAY_TAGS_FIELDS  = ['id', 'key', 'value', 'type']
WAY_NODES_FIELDS = ['id', 'node_id', 'position']

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
# Function to clean XML node elements and return
# a Python Dictionary of the cleaned elements
# ================================================== #
def shape_node(element):

    # Nodes structure can have id, lat, lon, tags [key, value]
    # NODE_FIELDS      = ['id', 'lat', 'lon', 'user', 'uid', 'version', 'changeset', 'timestamp']
    # NODE_TAGS_FIELDS = ['id', 'key', 'value', 'type']

    node_element      = {}
    node_element_tags = []

    # Gather NODE FIELD attributes
    for item in NODE_FIELDS:
        if item in element.attrib:
            node_element[item] = element.attrib[item]

    # Gather all sub element tags
    for subelem in element:

        # TAG subelement
        if subelem.tag == "tag":
            node_element_tag          = {}
            node_element_tag['id']    = get_element_id(element)
            node_element_tag["type"]  = get_tag_type(subelem)
            node_element_tag["key"]   = get_tag_key(subelem)
            node_element_tag["value"] = get_tag_value(subelem)
            node_element_tags.append(node_element_tag)

    # clean the TIGER data gathered
    node_element_tags = clean_tiger_data(node_element_tags)

    # Clean Addresses
    node_element_tags = clean_addresses(node_element_tags)

    # Clean Zip Codes
    node_element_tags = clean_zip_codes(node_element_tags)

    return {'node': node_element, 'node_tags': node_element_tags}


# ================================================== #
# Function to clean XML way elements and return
# a Python Dictionary of the cleaned elements
# ================================================== #
def shape_way(element):

    # Way structure is an ordered list of nodes, also containing tags [key, value]
    # WAY_FIELDS       = ['id', 'user', 'uid', 'version', 'changeset', 'timestamp']
    # WAY_TAGS_FIELDS  = ['id', 'key', 'value', 'type']
    # WAY_NODES_FIELDS = ['id', 'node_id', 'position']

    way_element       = {}
    way_element_tags  = []
    way_element_nodes = []

    # Gather WAY FIELD attributes
    for item in WAY_FIELDS:
        if item in element.attrib:
            way_element[item] = element.attrib[item]

    # Gather all sub element tags
    for index, subelem in enumerate(element):

        # NODE subelement
        if subelem.tag == "nd":
            way_element_node             = {}
            way_element_node['id']       = get_element_id(element)
            way_element_node["node_id"]  = get_node_id(subelem)
            way_element_node["position"] = index
            way_element_nodes.append(way_element_node)

        # TAG subelement
        if subelem.tag == "tag":
            way_element_tag          = {}
            way_element_tag['id']    = get_element_id(element)
            way_element_tag["type"]  = get_tag_type(subelem)
            way_element_tag["key"]   = get_tag_key(subelem)
            way_element_tag["value"] = get_tag_value(subelem)
            way_element_tags.append(way_element_tag)

    # Clean the TIGER data gathered
    way_element_tags = clean_tiger_data(way_element_tags)

    # Clean Addresses
    way_element_tags = clean_addresses(way_element_tags)

    # Clean Zip Codes
    way_element_tags = clean_zip_codes(way_element_tags)

    return {'way': way_element, 'way_nodes': way_element_nodes, 'way_tags': way_element_tags}


# ================================================== #
# Function to clean TIGER data addresses and zip codes
# ================================================== #
def clean_tiger_data(list_of_tags):

    #TAGS_FIELDS = ['id', 'key', 'value', 'type']
    new_list_of_tags = []

    street_str   = []
    city_str     = ""
    id_str       = ""
    zipcode_str = ""

    for tag_item in list_of_tags:

        # TIGER data
        if tag_item["type"] == "tiger":

            # County <=> City
            if tag_item["key"] == "county":
                new_tag_item         = {}
                new_tag_item['type'] = "addr"
                new_tag_item['key']  = "county"
                new_tag_item['id']   = tag_item['id']
                if "," in  tag_item["value"]:
                    new_tag_item['value'] = tag_item["value"].split(",", 1)[0]
                else:
                    new_tag_item['value'] = tag_item["value"]
                new_list_of_tags.append(new_tag_item)

            # zipcode
            if tag_item["key"] == "zip_left":
                new_tag_item          = {}
                new_tag_item['type']  = "addr"
                new_tag_item['key']   = "postcode"
                new_tag_item['id']    = tag_item['id']
                new_tag_item['value'] = tag_item["value"]
                new_list_of_tags.append(new_tag_item)

            # street_address pt1"
            if tag_item["key"] == "name_direction_prefix":
                street_str.insert(0, tag_item["value"])

            # street_address pt2"
            if tag_item["key"] == "name_base":
                street_str.insert(1, tag_item["value"])

            # street_address pt3"
            if tag_item["key"] == "name_type":
                street_str.insert(2, tag_item["value"])

        # Non Tiger item, don't change
        else:
            new_list_of_tags.append(tag_item)

        # Add an item of the joined street address
    if (len(street_str) != 0):
        new_tag_item          = {}
        new_tag_item['type']  = "addr"
        new_tag_item['key']   = "street"
        new_tag_item['id']    = tag_item['id']
        new_tag_item['value'] = " ".join(street_str)
        new_list_of_tags.append(new_tag_item)

    return new_list_of_tags


# ================================================== #
# Function to get "id" from element or throw error
# ================================================== #
def get_element_id(elem):

    if "id" in elem.attrib:
        return elem.attrib['id']
    else:
        print elem
        print "ERROR: Check element, missing 'id' attribute"


# ================================================== #
# Function to get "ref" from element or throw error
# ================================================== #
def get_node_id(elem):

    if "ref" in elem.attrib:
        return elem.attrib["ref"]
    else:
        print elem
        print "ERROR: Check element, missing 'ref' attribute"


# ================================================== #
# Function to get "type" from a node/way tag
# ================================================== #
def get_tag_type(elem):

    if "k" in elem.attrib:

        tag = elem.attrib["k"]

        if ":" in tag:
            return tag.split(":", 1)[0]
        else:
            return "regular"
    else:
        print "ERROR: Check get_tag_type() element does not have 'k' attribute"

# ================================================== #
# Function to get "key" from a node/way tag
# ================================================== #
def get_tag_key(elem):

    if "k" in elem.attrib:

        tag = elem.attrib["k"]

        if ":" in tag:
            return tag.split(":", 1)[1]
        else:
            return tag
    else:
        print "ERROR: Check get_tag_key() element does not have 'k' attribute"


# ================================================== #
# Function to get "value" from a node/way tag
# ================================================== #
def get_tag_value(elem):

    if 'k' and 'v' in elem.attrib:
        return elem.attrib['v']
    else:
        print "ERROR: Check get_tag_value() element does not have expected attributes"


# ================================================== #
# Function to clean address names of mistakes
# ================================================== #
def clean_addresses(list_of_tags):

    for item in list_of_tags:

        # Street name
        if (item['key'] == "street"):
            item['value'] = fix_street_name(item['value'], MAPPING)

    return list_of_tags


# ================================================== #
# Function to clean zip codes of mistakes
# ================================================== #
def clean_zip_codes(list_of_tags):

    for item in list_of_tags:
        if(item['key'] == "postcode"):

            # Assign the postcode to a local variable
            postcode = item['value']

            # Remove whitespace to standardize format
            postcode = remove_whitespace(postcode)

            # Standardize each postcode format

            if (len(postcode) == 5
                and is_postcode_valid(postcode)):

                # Standard 5 digit postcode
                item['value'] = postcode

            elif (len(postcode) == 10
                  and postcode[5] == "-"
                  and is_postcode_valid(postcode[:5])):

                # Grab 5 digits from ZIP+4 format
                item['value'] = postcode[:5]


            elif (len(postcode) == 7
                  and postcode[:2] == "CO"
                  and is_postcode_valid(postcode[2:])):

                # Correct zip code in format "CO80214"
                item['value'] = postcode[2:]

            elif (len(postcode) == 14
                  and postcode[:9] == "Golden,CO"
                  and is_postcode_valid(postcode[9:])):

                # Correct zip code in format "Golden, CO 80401"
                item['value'] = postcode[9:]

            elif (";" in postcode):

                # Add all valid postalcode values if multiples listed
                for new_postcode in postcode.split(';'):
                    new_tag = item.copy()
                    new_tag['value'] = new_postcode
                    if(is_postcode_valid(new_postcode)):
                        list_of_tags.append(new_tag)
                list_of_tags.remove(item)

            elif (":" in postcode):

                # Add all valid postalcode values if range listed
                for new_postcode in range(int(postcode.split(':')[0]), int(postcode.split(':')[1])):
                    new_tag = item.copy()
                    new_tag['value'] = str(new_postcode)
                    if (is_postcode_valid(str(new_postcode))):
                        list_of_tags.append(new_tag)
                list_of_tags.remove(item)

            else:

                # Display the bad postcodes
                print "Bad postcode: " + postcode

                # Remove bad postal code
                list_of_tags.remove(item)

    return list_of_tags


# ================================================== #
# Function to check if a postal code is valid
# ================================================== #
def is_postcode_valid(postcode_str):

    if (len(postcode_str) == 5 and postcode_str[:2] == "80"):
        return True
    else:
        print "Invalid postcode: " + postcode_str
        return False


# ================================================== #
# Function to remove all whitespaces from a string
# ================================================== #
def remove_whitespace(string_in):
    return string_in.replace(" ", "")


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
# Function to fix issues found in the audit and
# write the clean data out to csv files
# ================================================== #
def process_map(file_in):

    with codecs.open(NODES_PATH,     'w') as nodes_file, \
         codecs.open(NODE_TAGS_PATH, 'w') as nodes_tags_file, \
         codecs.open(WAYS_PATH,      'w') as ways_file, \
         codecs.open(WAY_NODES_PATH, 'w') as way_nodes_file, \
         codecs.open(WAY_TAGS_PATH,  'w') as way_tags_file:

        nodes_writer     = UnicodeDictWriter(nodes_file,      NODE_FIELDS)
        node_tags_writer = UnicodeDictWriter(nodes_tags_file, NODE_TAGS_FIELDS)
        ways_writer      = UnicodeDictWriter(ways_file,       WAY_FIELDS)
        way_nodes_writer = UnicodeDictWriter(way_nodes_file,  WAY_NODES_FIELDS)
        way_tags_writer  = UnicodeDictWriter(way_tags_file,   WAY_TAGS_FIELDS)

        nodes_writer.writeheader()
        node_tags_writer.writeheader()
        ways_writer.writeheader()
        way_nodes_writer.writeheader()
        way_tags_writer.writeheader()

        for element in get_element(file_in, tags=('node', 'way')):

            # Clean and write out the NODES
            if ( element.tag == 'node'):
                el = shape_node(element)
                nodes_writer.writerow(el['node'])
                node_tags_writer.writerows(el['node_tags'])

            # Clean and write out the WAYS
            elif ( element.tag == 'way'):
                el = shape_way(element)
                ways_writer.writerow(el['way'])
                way_nodes_writer.writerows(el['way_nodes'])
                way_tags_writer.writerows(el['way_tags'])


# ================================================== #
# Main()
# ================================================== #
if __name__ == "__main__":
    print("Running...")
    process_map(OSM_FILE)
