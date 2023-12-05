import json
from shapely.geometry import LineString, Polygon
from shapely.geometry.geo import mapping
from shapely.geometry import shape

def convert_line_to_polygon(line_coords):
    line = LineString(line_coords)
    
    polygon = Polygon(line_coords)
    
    return polygon

def convert_geojson_line_to_polygon(geojson_path):
    with open(geojson_path, 'r') as file:
        geojson_data = json.load(file)

    for feature in geojson_data['features']:
        geometry_type = feature['geometry']['type']
        if geometry_type == 'LineString':
            line_coords = feature['geometry']['coordinates']
            polygon = convert_line_to_polygon(line_coords)
            
            feature['geometry']['type'] = 'Polygon'
            feature['geometry']['coordinates'] = mapping(polygon)['coordinates']

    output_path = geojson_path.replace('.geojson', '_modified.geojson')
    with open(output_path, 'w') as output_file:
        json.dump(geojson_data, output_file, indent=2)


def calculate_polygon_area(geojson_path):
    with open(geojson_path, 'r') as file:
        geojson_data = json.load(file)

    for feature in geojson_data['features']:
        geometry_type = feature['geometry']['type']
        if geometry_type == 'Polygon':
            polygon = shape(feature['geometry'])
            area = polygon.area
            feature['properties']['area'] = area

    output_path = geojson_path.replace('.geojson', '_with_area.geojson')
    with open(output_path, 'w') as output_file:
        json.dump(geojson_data, output_file, indent=2)



geojson_path = './data/area[landuse=residential].geojson'
geojson_path_modified = './data/area[landuse=residential]_modified.geojson'
convert_geojson_line_to_polygon(geojson_path)
calculate_polygon_area(geojson_path_modified)