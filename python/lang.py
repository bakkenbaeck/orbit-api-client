#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Detect the language of a text

API-Key and text are submitted in JSON body of request

"""

import sys
import json

try:
    import requests
except:
    print "We require the excellent requests library! Try: pip install requests"


if len(sys.argv)<2:
    print "Usage: lang.py <api-key>"
    sys.exit(1)

api_key = sys.argv[1]

no_text = """Sør-Afrika: Takket være et mål i siste liten av Sami Khedira, tok
Tyskland bronsen under Fotball-VM 2010 i Sør-Afrika."""



response = requests.post('http://api.orbitapi.com/lang',
                         data=json.dumps(dict(api_key=api_key, text=no_text)),
                         headers = {'content-type': 'application/json'})

if response.status_code == requests.codes.ok:
    print json.dumps(response.json(), sort_keys=True, indent=4, separators=(',', ': '))
else:
    print "Error", response.status_code, response.text
