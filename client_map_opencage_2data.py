import pandas as pd
import plotly.express as px
from geopy.geocoders import OpenCage

# Mapbox token and OpenCage API key
token = 'pk.eyJ1Ijoib3ZhbmRvY2FydGVyIiwiYSI6ImNsODZqZW1xNTAwMnMzd24zZWI2OXlkZGkifQ.rb-Zu7HeLzPglir-n9Z1lQ'
opencage_key = 'cf490a6331f34c79aa6fcedf8d4b0213'  

# Initialize OpenCage geocoder
geolocator = OpenCage(api_key=opencage_key)

# Function to retrieve latitude and longitude from postcode
def get_lat_lon(postcode):
    try:
        location = geolocator.geocode(postcode)
        if location:
            return location.latitude, location.longitude
    except Exception as e:
        print(f"Error fetching data for postcode {postcode}: {e}")
    return None, None

# Read two different datasets
post_df1 = pd.read_csv("./postcodes_SE_London3.csv", sep=",")
post_df2 = pd.read_csv("./client_sites.csv", sep=",")

# Apply the function to create latitude and longitude columns for both datasets
post_df1["latitude"], post_df1["longitude"] = zip(*post_df1["PostCode"].apply(get_lat_lon))
post_df2["latitude"], post_df2["longitude"] = zip(*post_df2["PostCode"].apply(get_lat_lon))

# Drop rows with missing latitude or longitude
post_df1 = post_df1.dropna(subset=["latitude", "longitude"])
post_df2 = post_df2.dropna(subset=["latitude", "longitude"])

# Add a 'source' column to identify which dataset the data is from
post_df1["source"] = "Accademy Clients"
post_df2["source"] = "Collaborator Site"

# Concatenate the two datasets
combined_df = pd.concat([post_df1, post_df2])

# Group by latitude and longitude to count occurrences per dataset
grouped_df = combined_df.groupby(["latitude", "longitude", "source"]).size().reset_index(name='qty')

# Plot the data on the map, using the 'source' column to color by dataset
fig = px.scatter_mapbox(grouped_df, 
                        lat="latitude", 
                        lon="longitude", 
                        color="source",  # Different colors for each dataset
                        color_discrete_sequence=["fuchsia", "blue"],  # Specify colors
                        size='qty',
                        zoom=12, 
                        height=800,
                        title='London Parkour Project Clients by Dataset')

# Update map style and token
fig.update_layout(mapbox_style="dark", mapbox_accesstoken=token)
fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

# Show the plot
fig.show()
