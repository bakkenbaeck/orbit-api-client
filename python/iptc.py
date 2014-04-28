#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

Classify a text into the correct IPTC category

API-Key and text are submitted in JSON body of request

"""

import sys
import json

try:
    import requests
except:
    print "We require the excellent requests library! Try: pip install requests"


if len(sys.argv)<2:
    print "Usage: iptc.py <api-key>"
    sys.exit(1)

api_key = sys.argv[1]

text = """Sør-Afrika: Takket være et mål i siste liten av Sami Khedira, tok
Tyskland bronsen under Fotball-VM 2010 i Sør-Afrika.

Uruguay og Tyskland møttes i bronsefinalen i Fotball-VM 2010, den
10. juli 2010, i Port Elizabeth. Etter nitten minutter tok Tyskland
ledelsen etter at Thomas Muller scoret det første målet i kampen.

Stillingen til pause var 1-1, etter at Edinson Cavani scoret et mål,
ni minutter etter Tysklands mål. Seks minutter etter pause tok Uruguay
ledelsen, da Diego Forlán scoret sitt femte mål i VM. Seks minutter
etter Forláns mål, scoret Tyskland igjen da Marcell Jansen headet
ballen i mål etter et innlegg fra Jerome Boateng.

Med kun åtte minutter igjen av spilletid, scoret Sami Khedira
Tysklands seiersmål. I de siste sekundene av tillegstiden fikk Diego
Forlán et frispark, som endte opp med å treffe tverrliggeren, noe som
endte opp med at Tyskland tok bronsen, mens Uruguay tok fjerdeplassen.
"""

response = requests.post('http://api.orbitapi.com/iptc',
                         data=json.dumps(dict(api_key=api_key, text=text)),
                         headers = {'content-type': 'application/json'})

if response.status_code == requests.codes.ok:
    print json.dumps(response.json(), sort_keys=True, indent=4, separators=(',', ': '))
else:
    print "Error", response.status_code, response.text
