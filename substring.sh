#!/bin/bash

if [ $# -ne 3 ]; then
  echo "Используйте: $0 <исходная_строка> <первый_символ> <последний_символ>"
  exit 1
fi

src_str=$1
start_pos=$2
end_pos=$3

len=${#src_str}

if [ $start_pos -le 0 ] || [ $end_pos -gt $len ] || [ $start_pos -gt $end_pos ]; then
  echo "Некорректные параметры!!"
  exit 1
fi

substring=$(echo "$src_str" | cut -c "$start_pos-$end_pos")

echo "Подстрока $start_pos:$end_pos: '$substring'."

