# pip3.9 install folium
import folium
# dir(folium)

# create a map object
map = folium.Map(location=[39, -111], zoom_start="6", tiles="Stamen Terrain")

# FeatureGroup
fg = folium.FeatureGroup(name="Utah Map")

# add Marker to map
# fg.add_child(folium.Marker(location=[40.3,-111.7], popup="Vineyard", icon=folium.Icon(color="red")))
marker_coords = [[40.3, -111.7], [40.6, -111.4], [37, -113.5]]
marker_popups = ["Vineyard", "Park City", "St. George"]

# zip returns a zip object that is an iterator of tuples where the value in each tuple is paried together
for coords, popup in zip(marker_coords, marker_popups):
    fg.add_child(folium.Marker(location=coords, popup=popup, icon=folium.Icon(color="red")))

# add FeatureGroup marker to map object
map.add_child(fg)

# generate html map
map.save("app2/map.html")


