import overpy
from QueryToGeojson import convert_ways_to_geojson
from QueryToGeojson import convert_nodes_to_geojson
from QueryToGeojson import write_geojson
from OverpassQuery import *
import datetime


api = overpy.Overpass()

current_date = datetime.datetime.now().strftime("%Y-%m-%d")

queries = [query1, query2]


for index, query in enumerate(queries):

    output_filename = f"query_{index}_{current_date}"

    if query.strip().endswith("out geom;"):

        geojson = convert_ways_to_geojson(query, api)
        write_geojson(geojson, output_filename)

    elif query.strip().endswith("out;"):

        geojson = convert_nodes_to_geojson(query, api)
        write_geojson(geojson, output_filename)
    
    else:
        print("Query can't be processed")

