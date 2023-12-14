#!/bin/bash

directory=$2
extension=$3
output_file=$1

if [ ! -d "$directory" ]; then
    echo "Ошибка: Каталог '$directory' не существует."
    exit 1
fi

if [ ! -r "$directory" ]; then
    echo "Ошибка: Нет доступа к чтению каталога '$directory'."
    exit 1
fi

find "$directory" -type f -name "*.$extension" > "$output_file"
echo "Имена файлов с расширением .$extension из каталога $directory сохранены в $output_file"
