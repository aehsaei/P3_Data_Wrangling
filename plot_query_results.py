
import seaborn           as sns
import pandas            as pd
import sqlite3

db = sqlite3.connect('/Users/aehsaei/Desktop/DataAnalyst/Project3/denver_osm.db')
cursor = db.cursor()

# SQL command to find the top 10 amenities in Denver/Boulder
cursor.execute('''SELECT tags.value, COUNT(*) as count
                  FROM (SELECT * FROM node_tags
                        UNION ALL
                        SELECT * FROM way_tags) tags
                  WHERE tags.key='amenity'
                  GROUP BY tags.value
                  ORDER BY count DESC LIMIT 10''')

db.commit()
natural_df = pd.DataFrame(cursor.fetchall())

# Create the labels for the dataframe
natural_df.columns = ['Amenity', 'Amount']
print natural_df

# Remove 'Parking' since it's so much larger than all others
natural_df.drop(natural_df.head(1).index, inplace=True)

sns.set_style("whitegrid")
ax = sns.barplot(x="Amenity", y="Amount", data=natural_df)
sns.plt.show()


# Now plot the mountain peak data (not using direct SQL, this required a few SQL commands)
data = [{'Mountain Peak': 'Longs',         'Elevation (Meters)': 4340},
        {'Mountain Peak': 'Evans',         'Elevation (Meters)': 4335},
        {'Mountain Peak': 'Bierstadt',     'Elevation (Meters)': 4282},
        {'Mountain Peak': 'Meeker',        'Elevation (Meters)': 4227},
        {'Mountain Peak': 'Spalding',      'Elevation (Meters)': 4222},
        {'Mountain Peak': 'Gray Wolf',     'Elevation (Meters)': 4148},
        {'Mountain Peak': 'Rosalie',       'Elevation (Meters)': 4138},
        {'Mountain Peak': 'Epaulet',       'Elevation (Meters)': 4126},
        {'Mountain Peak': 'Chiefs Head',   'Elevation (Meters)': 4121},
        {'Mountain Peak': 'North Arapaho', 'Elevation (Meters)': 4100}]

mountains_df = pd.DataFrame(data)
print "\n\n"
print mountains_df
sns.set_style("whitegrid")
ax = sns.barplot(x="Mountain Peak", y="Elevation (Meters)", data=mountains_df)
sns.plt.ylim(4050, 4350)
sns.plt.show()