import csv
import requests
import pandas as pd
import plotly.express as px
from geopy.geocoders import OpenCage

# Token for Mapbox, using night mode
token = 'pk.eyJ1Ijoib3ZhbmRvY2FydGVyIiwiYSI6ImNsODZqZW1xNTAwMnMzd24zZWI2OXlkZGkifQ.rb-Zu7HeLzPglir-n9Z1lQ'

# OpenCage API key
opencage_key = 'cf490a6331f34c79aa6fcedf8d4b0213'  # Replace with your OpenCage API key

# Initialize OpenCage geocoder
geolocator = OpenCage(api_key=opencage_key)

# Read the CSV file
post_df = pd.read_csv("./postcodes_SE_London3.csv", sep=",")
print(post_df)

# Function to retrieve latitude and longitude from postcode using OpenCage
def get_lat_lon(postcode):
    try:
        location = geolocator.geocode(postcode)
        if location:
            return location.latitude, location.longitude
    except Exception as e:
        print(f"Error fetching data for postcode {postcode}: {e}")
    return None, None

# Apply the function to create latitude and longitude columns
post_df["latitude"], post_df["longitude"] = zip(*post_df["PostCode"].apply(get_lat_lon))

print(post_df)

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
