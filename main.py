import overpy
from QueryToGeojson import convert_ways_to_geojson
from QueryToGeojson import convert_nodes_to_geojson
from QueryToGeojson import write_geojson
from OverpassQuery import *


api = overpy.Overpass()

queries = [query1, query2]


for query in queries:

    if query.strip().endswith("out geom;"):

        geojson = convert_ways_to_geojson(query, api)
        write_geojson(geojson, "allo")

    elif query.strip().endswith("out;"):

        geojson = convert_nodes_to_geojson(query, api)
        write_geojson(geojson, "2")

