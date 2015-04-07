#!/bin/bash

if [ -z $1 ] ; then
   echo "Usage: shorttext.sh <orbit-api-key>"
   exit 1
fi

# Parameters in JSON body

time curl -X POST -H "Content-Type: application/json" -d "{ \"text\": \"Jeg liker politikk sier Solberg til VG.\" , \"api_key\": \"$1\" }" http://api.orbitapi.com/tag | python -m json.tool
