import geojson
from decimal import Decimal

def convert_nodes_to_geojson(query, api):

    result = api.query(query)

    features = []
    for node in result.nodes:
        lat = float(node.lat) 
        lon = float(node.lon)
        feature = geojson.Feature(
            geometry=geojson.Point((lon, lat)),
            properties={"id": node.id}
        )
        features.append(feature)

    feature_collection = geojson.FeatureCollection(features)

    geojson_string = geojson.dumps(feature_collection, sort_keys=True)

    return geojson_string


def convert_ways_to_geojson(query, api):

    result = api.query(query)
    ways = result.get_ways()

    geojson_data = {
        "type": "FeatureCollection",
        "features": []
    }   

    for way in ways:
        geometry = {
            "type": "LineString",
            "coordinates": []
        }
        for node in way.get_nodes(resolve_missing=True):
            lat, lon = float(node.lat), float(node.lon)
            geometry["coordinates"].append([lon, lat])

        feature = {
            "type": "Feature",
            "properties": {},
            "geometry": geometry
        }

        geojson_data["features"].append(feature)

    geojson_string = geojson.dumps(geojson_data, indent=2)

    return geojson_string


def write_geojson(geojson, output_filename):
     with open(f"./data/{output_filename}.geojson", "w") as output_file:
         output_file.write(geojson)








