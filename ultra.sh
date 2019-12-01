#!/bin/bash


for i in {1..12}; do

  times=$(date +%s);
  timestamp_="$times""000000000";
  value=$(python /home/pi/dev/Raspberry/ultrasonic_distance.py);

  curl -i -XPOST "http://192.168.1.155:8086/write?db=datacenters" --data-binary "ultra,home=piltza43 value=$value $timestamp_";

  sleep 5; 
done
