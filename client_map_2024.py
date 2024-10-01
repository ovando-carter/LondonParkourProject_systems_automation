import csv
import requests
import urllib.parse
import pandas as pd
import plotly.express as px

# Token taken from mapbox, using night mode
token = 'pk.eyJ1Ijoib3ZhbmRvY2FydGVyIiwiYSI6ImNsODZqZW1xNTAwMnMzd24zZWI2OXlkZGkifQ.rb-Zu7HeLzPglir-n9Z1lQ'

# Read the CSV file
post_df = pd.read_csv("./postcodes_SE_London3.csv", sep=",")

print(post_df)

# Function to retrieve latitude and longitude from postcode
def get_lat_lon(postcode):
    try:
        response = requests.get('https://nominatim.openstreetmap.org/search.php?q=' + urllib.parse.quote(postcode) + '&format=jsonv2')
        if response.status_code == 200:
            data = response.json()
            if data:
                return pd.to_numeric(data[0]["lat"]), pd.to_numeric(data[0]["lon"])
    except Exception as e:
        print(f"Error fetching data for postcode {postcode}: {e}")
    return None, None

# Apply the function to create latitude and longitude columns
post_df["latitude"], post_df["longitude"] = zip(*post_df["PostCode"].apply(get_lat_lon))

# Remove rows with missing latitude or longitude
post_df = post_df.dropna(subset=["latitude", "longitude"])

# Group by latitude and longitude to count occurrences
group_by_df = post_df.groupby(["latitude", "longitude"]).size().reset_index(name='qty')

# Plot the data on the map
fig = px.scatter_mapbox(group_by_df, 
                        lat="latitude", 
                        lon="longitude", 
                        color_discrete_sequence=["fuchsia"],
                        size='qty',
                        zoom=12, 
                        height=800,
                        title='London Parkour Project Clients')



fig.update_layout(mapbox_style="dark", mapbox_accesstoken=token)
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
fig.show()
