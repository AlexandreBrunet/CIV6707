
### Projet Overpass Interaction with OpenStreetMap
## Présentation
Projet réalisé dans le cadre d'un cours visant à interagir avec Overpass Turbo pour effectuer des requêtes sur OpenStreetMap. Le code est implémenté en Python en utilisant la bibliothèque overpy.

## Fonctionnement
Pour utiliser le projet, suivez ces étapes simples :

Ajoutez les requêtes souhaitées dans le fichier overpassquery.py

Exécutez le fichier main.py avec la commande suivante :
```console
python3 main.py
```
Une fois le code exécuté, les résultats des requêtes seront sauvegardés dans le dossier data au format GeoJSON.

## TODO
 Gérer différents types de géométries :
 * - [x] Point 
 * - [x] LineString
 * - [x] Polygon
 * - [ ] MultiPoint
 * - [ ] MultiLineString
 * - [ ] MultiPolygon