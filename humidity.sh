#!/bin/bash

times=$(date +%s)
timestamp_="$times""000000000"

array=()

while read line ; do
  array+=($line)
done < <(python /home/pi/dev/Raspberry/humidity.py)

#echo ${array[@]}

echo "L: $timestamp_"

curl -i -XPOST "http://192.168.1.155:8086/write?db=datacenters" --data-binary "humiditi,home=piltza43 value=${array[1]} $timestamp_"

curl -i -XPOST "http://192.168.1.155:8086/write?db=datacenters" --data-binary "temp2,home=piltza43 value=${array[0]} $timestamp_"
