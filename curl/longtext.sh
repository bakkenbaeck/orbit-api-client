#!/bin/bash

if [ -z $1 ] ; then
   echo "Usage: info <orbit-api-key>"
   exit 1
fi

# Parameters as Form values

time curl -v -v -X POST --form api_key=$1 --form "text=@largetext.txt" http://api.orbitapi.com/tag | python -m json.tool
#time curl -v -v -X POST --form api_key=$1 --form text=@largetext.txt http://localhost:1235/tag | python -m json.tool
