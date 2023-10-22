import overpy
import QueryToGeojson

api = overpy.Overpass()

def node_query(polygone, tag):
    query = f"""
    node[{tag}]
        (poly:"{polygone}");
    out;
    """
    return query

def way_query(polygone: str, key: str, value: str):
    query = f"""
    way[{key}={value}]
        (poly:"{polygone}");
    out geom;
    """
    return query

def node_counter(query):
    counter = api.query(query)
    nodes = len(counter.nodes)
    return nodes

def way_counter(query):
    counter = api.query(query)
    ways = len(counter.ways)
    return ways


def process_tags(polygone, tags, tag_type):
    for tag in tags:
        query = node_query(polygone, tag) if tag_type == "node" else way_query(polygone, tag.split('=')[0], tag.split('=')[1])
        num_items = node_counter(query) if tag_type == "node" else way_counter(query)
        if num_items == 0:
            print(f"No items found for {tag_type}: {tag}")
        else:
            print(f"Number of {tag_type}: {tag}: {num_items}")
            geojson_result = QueryToGeojson.convert_nodes_to_geojson(query, api) if tag_type == "node" else QueryToGeojson.convert_ways_to_geojson(query, api)
            QueryToGeojson.write_geojson(geojson_result, tag)
