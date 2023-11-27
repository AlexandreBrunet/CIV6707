import overpy
from querytogeojson import convert_to_geojson
from querytogeojson import write_geojson
from overpassquery import queries
import os
from analysis import GeoAnalysis
from shapely.geometry import shape
import json


api = overpy.Overpass()

folder = "./data"

for query_name, query_content in queries.items():

    output_file_name = query_content.strip().split('\n')[0]

    file = os.path.join(folder, output_file_name + ".geojson")

    if os.path.exists(file):
        print(f"The file {file} exists.")

    else:
        print(f"writing file: {query_name}, {file}")
        geojson = convert_to_geojson(query_content, api)
        write_geojson(geojson, output_file_name)