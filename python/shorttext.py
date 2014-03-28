#!/usr/bin/env python

"""

Tag a small chunk of text with Orbit API

API-Key and text are submitted in JSON body of request

"""

import sys
import json

try:
    import requests
except:
    print "We require the excellent requests library! Try: pip install requests"


if len(sys.argv)<2:
    print "Usage: smalltext.py <api-key>"
    sys.exit(1)

api_key = sys.argv[1]

response = requests.post('http://api.orbitapi.com/tag',
                         data=json.dumps(dict(api_key=api_key, text="Jeg liker politikk sa Solberg til VG.")),
                         headers = {'content-type': 'application/json'})

if response.status_code == requests.codes.ok:
    print json.dumps(response.json(), sort_keys=True, indent=4, separators=(',', ': '))
else:
    print "Error", response.status_code, response.text
