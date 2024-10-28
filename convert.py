#!/bin/env python

import json, argparse
import geojson

parser = argparse.ArgumentParser(description="Barebones script to convert ED-269 JSON to GeoJSON")
parser.add_argument('FILE', help="ED-269 Input File") #Re-used as paste ID or URL when deleting
args = vars(parser.parse_args())

ed269 = None
with open(args['FILE'], 'r') as fd:
    ed269 = json.load(fd)

features = []
for f in ed269['features']:
    geometries = []

    properties = {}
    for p in f.keys():
        if p != 'geometry':
            properties[p] = f[p]

    for g in f['geometry']:
        gproj = g['horizontalProjection']
        match gproj['type']:
            case 'Circle':
                geometries.append(geojson.Point(gproj['center']))
                properties['radius'] = gproj['radius']
            case 'Polygon':
                geometries.append(geojson.Polygon(gproj['coordinates']))
    if len(geometries) > 1:
        geometry = geojson.GeometryCollection(geometries)
    else:
        geometry = geometries[0]
    feature = geojson.Feature(id=f['identifier'], geometry=geometry, properties=properties)
    features.append(feature)

fc = geojson.FeatureCollection(features)

print(fc)
