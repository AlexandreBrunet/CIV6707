import overpy

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
