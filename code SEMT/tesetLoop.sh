#!/bin/bash
x=0
until [ "$x" -ge 10 ]; do
    echo "Current value of x: $x"
    x=$(expr $x + 1)
    sleep 1
done
