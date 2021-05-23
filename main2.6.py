# Instead of this:
# from geopy.geocoders import Nominatim
# nom = Nominatim()

# Use this:
# pip3.9 install geopy
# from geopy.geocoders import ArcGIS
# nom = ArcGIS()

# from geopy.geocoders import ArcGIS

# arc = ArcGIS()
# coords = arc.geocode("3995 23rd St, San Francisco, CA 94114")
# coords.latitude
# coords.longitude

# import pandas
# df = pandas.read_csv("supermarkets.csv")
# df["Address"] = df["Address"] + ", " + df["City"] + ", " + df["State"] + ", " + df["Country"]
# df["Coordinates"] = df["Address"].apply(arc.geocode)
# df["Latitude"] = df["Coordinates"].apply(lambda x: x.latitude if x != None else None)
# df["Longitude"] = df["Coordinates"].apply(lambda x: x.longitude if x != None else None)
# df