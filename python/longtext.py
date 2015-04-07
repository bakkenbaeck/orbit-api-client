#!/usr/bin/env python

"""

Tag a large chunk of text with Orbit API

API-Key and text are submitted as a multipart form

"""

import sys
import json

try:
    import requests
except:
    print "We require the excellent requests library! Try: pip install requests"


if len(sys.argv)<2:
    print "Usage: longtext.py <api-key>"
    sys.exit(1)

api_key = sys.argv[1]

response = requests.post('http://api.orbitapi.com/tag',
                         data=dict(api_key=api_key),
                         files=dict(text=file('largetext.txt'))
                         )

if response.status_code == requests.codes.ok:
    print json.dumps(response.json(), sort_keys=True, indent=4, separators=(',', ': '))
else:
    print "Error", response.status_code, response.text
