#!/bin/bash

if [ $# -ne 2 ]; then
  echo "Используйте: $0 <имя_файла> <новое_расширение>"
  exit 1
fi

filename=$1
new_extension=$2

if [[ $filename != *.* ]]; then
  echo "Файл '$filename' не имеет расширения."
  exit 1
fi

basename=$(basename "$filename")

filename_no_ext="${basename%.*}"

new_filename="$filename_no_ext.$new_extension"

mv "$filename" "$new_filename"

echo "Расширение файла '$filename' успешно изменено на '$new_extension'. Новое имя файла: '$new_filename'."

