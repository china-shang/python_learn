#!/bin/bash
a=4
while [ $a -gt 0 ]
do
    sleep 1
    let "a=$a-1"
    echo "start" $a
done
