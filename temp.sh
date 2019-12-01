#!/bin/bash

times=$(date +%s)
timestamp_="$times""000000000"

value=$(python /home/pi/dev/Raspberry/temp.py)

curl -i -XPOST "http://192.168.1.155:8086/write?db=datacenters" --data-binary "temp,home=piltza43 value=$value $timestamp_"


