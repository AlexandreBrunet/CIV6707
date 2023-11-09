import overpy
from querytogeojson import convert_lines_to_geojson
from querytogeojson import convert_nodes_to_geojson
from querytogeojson import convert_to_geojson
from querytogeojson import write_geojson
from overpassquery import queries
import re
import os


api = overpy.Overpass()

for query_name, query_content in queries.items():

    output_file_name = query_content.strip().split('\n')[0]

    geojson = convert_to_geojson(query_content, api)
    write_geojson(geojson, output_file_name)

