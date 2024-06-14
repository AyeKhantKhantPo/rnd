#!/bin/bash

for ((i=0;i<=10;i++)); do
  if [ $(($i % 2)) -ne 1 ]; then
    continue
  fi
  echo $i
done