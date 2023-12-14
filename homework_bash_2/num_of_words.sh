#!/bin/bash

text_file="$1"

cat "$text_file" | tr -s '[:space:]' '\n' | grep -oE '([а-яА-Яa-zA-Z]+-?[а-яА-Яa-zA-Z]*)+' | wc -w
