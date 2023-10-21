import overpy
import geojson

def convert_nodes_to_geojson(query):
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


def convert_ways_to_geojson(query):
    
    api = overpy.Overpass()
    result = api.query(query)

    features = []

    # Iterate over ways in the result
    for way in result.ways:
        coords = []

        for node in way.nodes:
            lat = float(node.lat)
            lon = float(node.lon)
            coords.append((lon, lat))

        feature = geojson.Feature(
            geometry=geojson.LineString(coords),
            properties={"id": way.id}
        )
        features.append(feature)

    feature_collection = geojson.FeatureCollection(features)

    geojson_string = geojson.dumps(feature_collection, sort_keys=True)

    return geojson_string