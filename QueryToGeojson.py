import geojson
import overpy

def write_geojson(geojson, output_filename):
     with open(f"./data/{output_filename}.geojson", "w") as output_file:
         output_file.write(geojson)


def convert_element_to_geojson(element):
    if isinstance(element, overpy.Way):
        geometry_type = 'LineString'
        coordinates = [[float(node.lon), float(node.lat)] for node in element.get_nodes(resolve_missing=True)]
    elif isinstance(element, overpy.Node):
        geometry_type = 'Point'
        coordinates = [float(element.lon), float(element.lat)]
    elif isinstance(element, overpy.Relation) and element.tags.get('type') == 'multipolygon':
        geometry_type = 'Polygon'
        coordinates = [
            [
                [float(node.lon), float(node.lat)] for node in element.nodes
            ]
        ]
    else:
        # Ajouter d'autres geometry type si besoin
        return None
    
    properties = {"@id": element.id}
    properties.update(element.tags)

    if geometry_type == 'Point':
        geometry = geojson.Point(coordinates)
    elif geometry_type == 'LineString':
        geometry = geojson.LineString(coordinates)
    elif geometry_type == 'Polygon':
        geometry = geojson.Polygon(coordinates)
    else:
        return None

    feature = geojson.Feature(
        geometry=geometry,
        properties=properties
    )

    return feature


def convert_to_geojson(query, api):
    result = api.query(query)

    geojson_data = {
        "type": "FeatureCollection",
        "features": []
    }

    for element in result.nodes + result.ways + result.relations + result.areas:
        feature = convert_element_to_geojson(element)
        if feature:
            geojson_data["features"].append(feature)

    geojson_string = geojson.dumps(geojson_data, indent=2)

    return geojson_string








