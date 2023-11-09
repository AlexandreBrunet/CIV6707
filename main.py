import overpy
from querytogeojson import convert_lines_to_geojson
from querytogeojson import convert_nodes_to_geojson
from querytogeojson import write_geojson
from overpassquery import queries
import re
import os


api = overpy.Overpass()

for query_name, query_content in queries.items():

    if query_content.strip().endswith("out geom;"):

        pattern = r'way\[[^\]]+\]'
        output_filename = re.findall(pattern, query_content)[0]

        output_geojson = output_filename + ".geojson"
        file_path = os.path.join("./data", output_geojson)

        if os.path.exists(file_path):
            print(f"File {output_geojson} already exists")
        else:
            geojson = convert_lines_to_geojson(query_content, api)
            write_geojson(geojson, output_filename)

    elif query_content.strip().endswith("out;"):

        pattern = r'node\[[^\]]+\]'
        output_filename= re.findall(pattern, query_content)[0]
        
        output_geojson = output_filename + ".geojson"
        file_path = os.path.join("./data", output_geojson)

        if os.path.exists(file_path):
            print(f"File {output_geojson} already exists")
        else:
            geojson = convert_lines_to_geojson(query_content, api)
            write_geojson(geojson, output_filename)
    
    else:
        print("Query can't be processed")

