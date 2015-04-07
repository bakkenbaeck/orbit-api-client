#!/bin/bash

if [ -z $1 ] ; then
   echo "Usage: iptc_url.sh <orbit-api-key>"
   exit 1
fi

# Parameters in JSON body

url='http://www.vg.no/sport/fotball/landslaget/brasil-norge-1-2/a/19725/'

time curl -X POST -H "Content-Type: application/json" -d "{ \"url\": \"$url\" , \"api_key\": \"$1\" }" http://api.orbitapi.com/iptc | python -m json.tool
