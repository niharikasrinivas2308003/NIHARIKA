# Task: Geographic Analysis

import pandas as pd
task1 = 'C:\\Users\\nihar\\OneDrive\\Documents\\cognify techno intern\\Dataset .csv'
level = pd.read_csv(task1)
print(level)

# Plot the locations of restaurants on a map using longitude and latitude coordinates

import folium
m = folium.Map(location=[level['Latitude'].mean(), level['Longitude'].mean()], zoom_start=12)
for idx, row in level.iterrows():
  folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=row['Restaurant Name']  # Assuming there is a 'name' column for the restaurant name
    ).add_to(m)
m.save('restaurants_map.html')  

# Identify any patterns or clusters of restaurants in specific areas.
from sklearn.cluster import DBSCAN
import numpy as np
import folium
coords = level[['Latitude', 'Longitude']].values
db = DBSCAN(eps=0.01, min_samples=5, algorithm='ball_tree', metric='haversine').fit(np.radians(coords))
labels = db.labels_
level['cluster'] = labels

# Plot the clusters on the map
cluster_map = folium.Map(location=[level['Latitude'].mean(), level['Longitude'].mean()], zoom_start=12)

# Colors for clusters
colors = ['red', 'blue', 'green', 'purple', 'orange', 'darkred', 'lightred', 'beige', 'darkblue', 'darkgreen', 'cadetblue', 'darkpurple', 'white', 'pink', 'lightblue', 'lightgreen', 'gray', 'black', 'lightgray']

for idx, row in level.iterrows():
    folium.CircleMarker(
        location=[row['Latitude'], row['Longitude']],
        radius=5,
        color=colors[row['cluster'] % len(colors)],
        fill=True,
        fill_color=colors[row['cluster'] % len(colors)],
        popup=row['Restaurant Name']  # Assuming there is a 'name' column for the restaurant name
    ).add_to(cluster_map)

# Save the cluster map to an HTML file
cluster_map.save('restaurants_clusters_map.html')


