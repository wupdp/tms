#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Используйте $0 имя_файла"
    exit 1
fi

filename=$1

if [ ! -f "$filename" ]; then
    echo "Файл не найден."
    exit 1
fi

sed -i -E 's/(\b[[:alpha:]]+\b)[[:space:]]+\1/\1/g' "$filename"

echo "Повторы слов в файле $filename исправлены"
