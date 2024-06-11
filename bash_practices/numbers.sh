#!/bin/bash

num=(1 2 3 4 5)

echo ${num[*]}

unset num[2]
echo ${num[*]}

unset num

echo ${num[*]}
