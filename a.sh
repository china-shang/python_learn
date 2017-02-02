#!/bin/bash
a=4
while [ $a > 0 ]
do
    sleep 1
    a=expr ` $a-1 `
    echo "start" $a
done
