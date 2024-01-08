#!/bin/bash

for file in logs/*.log; do
    mv "$file" "${file%.log}_$(date +"%s").log"
done

for file in python/*.py; do
    mv "$file" "${file%.py}_$(git log -1 --format=%h).py"
done
