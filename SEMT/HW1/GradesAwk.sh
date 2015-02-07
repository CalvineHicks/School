#!/bin/bash
#Calvin Hicks
awk '{ for(i=3; i<=NF;i++) j+=$i; print (j/3),"["$1"]" ,$3",", $2; j=0 }' $1 | sort -k 3
