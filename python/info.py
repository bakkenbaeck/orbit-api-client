#!/usr/bin/env python

"""

Get account info from OrbitAPI

API-Key is passed as HTTP header.

"""

import sys
import json

try:
    import requests
except:
    print "We require the excellent requests library! Try: pip install requests"


if len(sys.argv)<2:
    print "Usage: info.py <api-key>"
    sys.exit(1)

api_key = sys.argv[1]

response = requests.get("http://api.orbitapi.com/info", headers={ "x-orbit-api-key": api_key })

if response.status_code == requests.codes.ok:
    print json.dumps(response.json(), sort_keys=True, indent=4, separators=(",", ": "))
else:
    print "Error", response.status_code, response.text
