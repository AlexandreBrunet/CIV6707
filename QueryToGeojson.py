import geojson
import overpy


def convert_to_geojson(query, api):
    result = api.query(query)

    geojson_data = {
        "type": "FeatureCollection",
        "features": []
    }

    for element in result.nodes + result.ways + result.relations + result.areas:
        if isinstance(element, overpy.Way):
            geometry_type = 'LineString'
            coordinates = [[float(node.lat), float(node.lon)] for node in element.get_nodes(resolve_missing=True)]
        else:
            geometry_type = element.geometry().type
            coordinates = [float(element.lat), float(element.lon)]

        if geometry_type == 'Point':
            geometry = geojson.Point(coordinates)
        elif geometry_type == 'LineString':
            geometry = geojson.LineString(coordinates)
        elif geometry_type == 'Polygon':
            coordinates = [[[float(node.lat), float(node.lon)] for node in element.nodes]]
            geometry = geojson.Polygon(coordinates)
        else:
            # Handle other geometry types if needed
            continue

        feature = geojson.Feature(
            geometry=geometry,
            properties={"@id": element.id}
        )
        geojson_data["features"].append(feature)

    geojson_string = geojson.dumps(geojson_data, indent=2)

    return geojson_string


def write_geojson(geojson, output_filename):
     with open(f"./data/{output_filename}.geojson", "w") as output_file:
         output_file.write(geojson)








