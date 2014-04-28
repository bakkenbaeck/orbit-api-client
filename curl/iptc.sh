#!/bin/bash

if [ -z $1 ] ; then
   echo "Usage: info <orbit-api-key>"
   exit 1
fi

# Parameters in JSON body

text='Uruguay og Tyskland møttes i bronsefinalen i Fotball-VM 2010, den 10. juli 2010, i Port Elizabeth. Etter nitten minutter tok Tyskland ledelsen etter at Thomas Muller scoret det første målet i kampen.'

time curl -X POST -H "Content-Type: application/json" -d "{ \"text\": \"$text\" , \"api_key\": \"$1\" }" http://api.orbitapi.com/iptc | python -m json.tool
