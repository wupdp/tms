#!/bin/bash

directory=$2
extension=$3
output_file=$1

find "$directory" -type f -name "*.$extension" > "$output_file"
echo "Имена файлов с расширением .$extension из каталога $directory сохранены в $output_file"
