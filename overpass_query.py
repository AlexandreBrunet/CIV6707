import overpy

def api_query(polygone, tag):
    api = overpy.Overpass()
    query = f"""
    node[{tag}]
        (poly:"{polygone}");
    out;
    """
    return query