import overpy
import geojson

def convert_query_to_geojson(query):
    api = overpy.Overpass()
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


def convert_way_to_geojson(query):
    api = overpy.Overpass()
    result = api.query(query)

    features = []
    for way in result.way:
        lat = float(way.lat) 
        lon = float(way.lon)
        feature = geojson.Feature(
            geometry=geojson.Point((lon, lat)),
            properties={"id": way.id}
        )
        features.append(feature)

    feature_collection = geojson.FeatureCollection(features)

    geojson_string = geojson.dumps(feature_collection, sort_keys=True)

    return geojson_string