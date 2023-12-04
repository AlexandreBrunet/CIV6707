import json
from geopy.distance import geodesic

def calculate_length(coordinates):
    length = 0
    for i in range(len(coordinates) - 1):
        point1 = coordinates[i]
        point2 = coordinates[i + 1]
        length += geodesic(point1, point2).meters
    return length

def filter_and_calculate_length(geojson_file_path):
    with open(geojson_file_path, 'r', encoding='utf-8') as file:
        geojson_data = json.load(file)

    cycleway_length = 0
    for feature in geojson_data['features']:
        properties = feature['properties']
        geometry = feature['geometry']
        if 'highway' in properties and properties['highway'] == 'footway':
            coordinates = geometry['coordinates']
            cycleway_length += calculate_length(coordinates)
    
    return cycleway_length


geojson_file_path = './data/way["highway"="footway"]["footway"="sidewalk"].geojson'

total_cycleway_length = filter_and_calculate_length(geojson_file_path) / 1000
print(f"Longueur totale {total_cycleway_length} km")