import json
import os
from shapely.geometry import shape
from geopy.distance import geodesic

folder_path = "./data"

longueur_totale_metres = 0.0

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
                    longueur_totale_metres += longueur_metres

            print(f"Nombre d'élements dans le ficher {filename}: {elements}",)
            print(f"Longueur totale des {filename} (mètre): {longueur_totale_metres}")