#!/bin/bash
#Calvin Hicks 
#(worked with Madison Rockwell)
sort -k 3,3 -k 2,2 $1 |
while IFS= read -r line; do
  AVG=$(echo "$line" | cut -d " " -f 4)
  NUMBER=$(echo "$line"| cut -d " " -f 1)
  FIRST=$(echo "$line"| cut -d " " -f 2)
  LAST=$(echo "$line"| cut -d " " -f 3)
  let AVG=AVG+$(echo "$line" | cut -d " " -f 5)
  let AVG=AVG+$(echo "$line" | cut -d " " -f 6)
  let AVG=AVG/3
  #echo "$line"
  echo "$AVG [$NUMBER] $LAST, $FIRST" #[$NAME] $3,$2
done #< "$1"
