# ed269-geojson
Convert ED-269 GeoZones into GeoJSON

This is a very barebones script to produce valid GeoJSON documents from ED-269 JSON files.

I do not have access to the ED-269 spec, so this is reversed engineered to work with the files I care about.

GeoJSON does not support circles, so I defined those as points with a `radius` property for the feature.


## Usage:

`convert.py [-h] FILE`

Where `FILE` is a valid ED-269 JSON document file (stdin is supported).
The script will output GeoJSON to stdout.
