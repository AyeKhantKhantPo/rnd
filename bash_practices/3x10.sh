#!/bin/bash

# while loop
num=1
while [ $num -le 10 ]; do
  echo $(($num * 3))
  num=$(($num+1))
done

# until loop
num=1
until [ $num -gt 10 ]; do
  echo $(($num * 3))
  num=$(($num+1))
done
