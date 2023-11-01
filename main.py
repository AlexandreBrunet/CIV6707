import overpy
from querytogeojson import convert_ways_to_geojson
from querytogeojson import convert_nodes_to_geojson
from querytogeojson import write_geojson
from overpassquery import *
import datetime
import re


api = overpy.Overpass()

current_date = datetime.datetime.now().strftime("%Y-%m-%d")

queries = [query1, query2]


for index, query in enumerate(queries):

    if query.strip().endswith("out geom;"):

        pattern = r'way\[[^\]]+\]'
        output_filename = re.findall(pattern, query)[0]

        geojson = convert_ways_to_geojson(query, api)
        write_geojson(geojson, output_filename)

    elif query.strip().endswith("out;"):

        pattern = r'node\[[^\]]+\]'
        output_filename= re.findall(pattern, query)[0]

        geojson = convert_nodes_to_geojson(query, api)
        write_geojson(geojson, output_filename)
    
    else:
        print("Query can't be processed")

