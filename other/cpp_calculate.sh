#!/bin/bash

file=$1

count=$(find $file \( -name '*.h' -o -name '*.cpp' \) -exec cat '{}' \; | wc -l)

echo "code lines: $count"
