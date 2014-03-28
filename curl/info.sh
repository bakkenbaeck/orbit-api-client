#!/bin/bash

if [ -z $1 ] ; then
   echo "Usage: info <orbit-api-key>"
   exit 1
fi

time curl -H "X-Orbit-Api-Key: $1" -H "Content-Type: application/json" http://api.orbitapi.com/info | python -m json.tool
