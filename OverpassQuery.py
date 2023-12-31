polygone = "45.503636789066604 -73.5194281357647 45.50411033703699 -73.51759820704044 45.5048206515236 -73.51759820704044 45.50626098394275 -73.51731667954446 45.507740739142946 -73.5172040685459 45.509496664844136 -73.51757005429104 45.51071986161344 -73.51793604003569 45.51239678172209 -73.51768266528913 45.513462093248904 -73.51768266528913 45.51488247724984 -73.51807680378367 45.51690115824721 -73.51911845551983 45.51881460581171 -73.52007564900632 45.52019540384018 -73.52013195450563 45.52102386639223 -73.520300871003 45.52187204160509 -73.52018826000491 45.52193121614235 -73.5186398587761 45.521457818098156 -73.51686623555113 45.52072798830986 -73.51565566731807 45.51913021977748 -73.51433248808645 45.51926830033031 -73.51365682209594 45.52011650200845 -73.51337529459998 45.52189176645774 -73.51337529459998 45.5274401148896 -73.51348790559919 45.52850514162543 -73.51331898910132 45.5289587580007 -73.51286854510747 45.529195425961234 -73.51340344734999 45.52970820312734 -73.5134597528493 45.53177898642866 -73.51917476101926 45.532015642522424 -73.51945628851571 45.532449509442245 -73.51951259401451 45.535530306549845 -73.51697884655135 45.53670293716485 -73.5160216530638 45.53784666558133 -73.51478293208136 45.5406861665914 -73.51089785263565 45.54167207090239 -73.509715437152 45.543525524204966 -73.51269962861055 45.54113968472194 -73.51948444126556 45.53193057791793 -73.52973204212235 45.52562231310475 -73.52683230891198 45.50450219496341 -73.52061055124797 45.503636789066604 -73.5194281357647"

queries = {
    "query1": f"""
        way[maxspeed=100]
            (poly:"{polygone}");
        out geom;
    """,
    "query2": f"""
        way[maxspeed=70]
            (poly:"{polygone}");
        out geom;
    """,
    "query3": f"""
        way[maxspeed=50]
            (poly:"{polygone}");
        out geom;
    """,
    "query4": f"""
        way[maxspeed=40]
        (poly:"{polygone}");
        out geom;
    """,
    "query5": f"""
        way[maxspeed=30]
        (poly:"{polygone}");
        out geom;
    """,
    "query6": f"""
        way[highway=cycleway]
        (poly:"{polygone}");
        out geom;
    """,
    # "query7": f"""
    #     way[highway=footway]
    #     (poly:"{polygone}");
    #     way[footway=sidewalk]
    #     (poly:"{polygone}");
    #     way[highway=path][foot=designated]
    #     (poly:"{polygone}");
    #     way[highway][sidewalk:both=yes]
    #     (poly:"{polygone}");
    #     way[highway][sidewalk:right=yes]
    #     (poly:"{polygone}");
    #     way[highway][sidewalk:left=yes]
    #     (poly:"{polygone}");
    #     out geom;
    # """,
    "query8": f"""
        node[highway=bus_stop]
        (poly:"{polygone}");
        out;
    """,
    "query9": f"""
        relation[type=route][route=bus]
        (poly:"{polygone}");
        out geom;
    """,
    # "query10": f"""
    #     node[amenity=parking]
    #     (poly:"{polygone}");
    #     area[amenity=parking]
    #     (poly:"{polygone}");
    #     out geom;
    # """,
    "query11": f"""
        node[amenity~"^college|school|university|kindergarten$"]
        (poly:"{polygone}");
        area[amenity~"^college|school|university|kindergarten$"]
        (poly:"{polygone}");
        out geom;
    """,
    "query12": f"""
        node[amenity=fuel]
        (poly:"{polygone}");
        area[amenity=fuel]
        (poly:"{polygone}");
        out geom;
    """,
    "query13": f"""
        node[amenity~"^clinic|dentist|doctors|hospital$"]
        (poly:"{polygone}");
        area[amenity~"^clinic|dentist|doctors|hospital$"]
        (poly:"{polygone}");
        out geom;
    """,
    "query14": f"""
        node[amenity=nursing_home]
        (poly:"{polygone}");
        area[amenity=nursing_home]
        (poly:"{polygone}");
        node[amenity=social_facility][social_facility=nursing_home]
        (poly:"{polygone}");
        area[amenity=social_facility][social_facility=nursing_home]
        (poly:"{polygone}");
    out geom;
    """,
    "query15": f"""
        node[amenity~"^arts_centre|cinema|community_centre|events_venue|music_venue|social_centre|theatre"]
        (poly:"{polygone}");
        area[amenity~"^arts_centre|cinema|community_centre|events_venue|music_venue|social_centre|theatre"]
        (poly:"{polygone}");
        out geom;
    """,
    "query16": f"""
        area[landuse~"^commercial|retail$"]
        (poly:"{polygone}");
        out geom;
    """,
    "query17": f"""
        area[landuse=industrial]
        (poly:"{polygone}");
        out geom;
    """,
    # "query18": f"""
    #     area[landuse=residential]
    #     (poly:"{polygone}");
    #     out geom;
    # """,
    "query19": f"""
        area[leisure=park]
        (poly:"{polygone}");
        out geom;
    """,
    "query20": f"""
        way[building=apartments]
            (poly:"{polygone}");
        out geom;
    """,
    "query21": f"""
        way[building=commercial]
            (poly:"{polygone}");
        out geom;
    """,
    "query22": f"""
        way[amenity=bus_station]
            (poly:"{polygone}");
        out geom;
    """,
    "query23": f"""
        way["highway"="footway"]["footway"="sidewalk"]
            (poly:"{polygone}");
        out geom;
    """,
    "query24": f"""
        way["highway"="footway"]
            (poly:"{polygone}");
        out geom;
    """,
    "query25": f"""
        node["amenity"="parking"]
            (poly:"{polygone}");
        way[amenity=parking]
            (poly:"{polygone}");
        relation["amenity"="parking"]
            (poly:"{polygone}");
        out geom;
    """,
    "query26": f"""
        way["landuse"="residential"]
            (poly:"{polygone}");
        out geom;
    """,
    "query27": f"""
        way["amenity"="parking"]
            (poly:"{polygone}");
        out geom;
    """,
    "query28": f"""
        way["amenity"="parking"]["type"="multipolygon"]
            (poly:"{polygone}");
        relation["amenity"="parking"]["type"="multipolygon"]
            (poly:"{polygone}");
        out body;
        >;
        out skel qt;    
    """,
    "query29": f"""
        node["amenity"="drinking_water"]
            (poly:"{polygone}");
        out;  
    """,
    "query30": f"""
        node["amenity"="bicycle_parking"]
            (poly:"{polygone}");
        out;  
    """,
    "query31": f"""
        node["amenity"="bench"]
            (poly:"{polygone}");
        out;  
    """,
    "query32": f"""
        node["amenity"="fast_food"]
            (poly:"{polygone}");
        out;  
    """,
    "query33": f"""
        node["amenity"="toilets"]
            (poly:"{polygone}");
        out;  
    """,
    "query33": f"""
        node[highway=crossing][crossing=unmarked]
            (poly:"{polygone}");
        out;  
    """,
    "query34": f"""
        node[highway=crossing][crossing=marked]
            (poly:"{polygone}");
        out;  
    """,
    "query35": f"""
        node[highway=crossing][crossing=traffic_signals]
            (poly:"{polygone}");
        out;  
    """,
    "query36": f"""
        node[highway=crossing][crossing=uncontrolled]
            (poly:"{polygone}");
        out;  
    """,
    "query37": f"""
        way[highway=residential]
            (poly:"{polygone}");
        out geom;  
    """,
    "query37": f"""
        area[landuse=residential]
            (poly:"{polygone}");
        out geom;  
    """,
    "query38": f"""
        area[landuse=commercial]
            (poly:"{polygone}");
        out geom;  
    """,
}

# TODO : Nombre de buildings résidentiels et nombre de ménages?
# TODO : Part de routes avec un trottoir
# TODO : Trouver d'autres idées d'analyses à faire
# Certains footway sont en area, à ajouter?
# Valider ajouts query7