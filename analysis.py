import json
import os
from shapely.geometry import shape
from geopy.distance import geodesic
import geopandas as gpd
import matplotlib.pyplot as plt

folder_path = "./data"

longueur_totale_km = 0.0

for filename in os.listdir(folder_path):
     if filename.endswith(".geojson"):
          file_path = os.path.join(folder_path, filename)
          with open(file_path, "r") as geojson_file:
            data = json.load(geojson_file)
            elements = len(data["features"])

            for feature in data["features"]:
                geometry = shape(feature["geometry"])
                if geometry.type == "LineString":
                    longueur_metres = geodesic((geometry.coords[0][::-1]), (geometry.coords[-1][::-1])).m
                    longueur_totale_km += longueur_metres/1000

            longueur_totale_km_rounded = round(longueur_totale_km, 2)

            print(f"Nombre d'élements dans le ficher {filename}: {elements}",)
            print(f"Longueur totale des {filename} : {longueur_totale_km_rounded} km")


            plt.bar(filename, longueur_totale_km_rounded)

plt.xlabel("GeoJSON Files")
plt.ylabel("Total Length (km)")
plt.title("Total Length in Kilometers for Each GeoJSON File")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()        