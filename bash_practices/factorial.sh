#!/bin/bash

factorial () {
  if [ $1 -le 1 ]; then
  echo 1
  else
  last=$(factorial $(( $1 - 1 )))
  echo $(( $1 * last ))
  fi
}

echo -n "4! is: "
factorial 4
echo -n "5! is: "
factorial 5
echo -n "6! is: "
factorial 6