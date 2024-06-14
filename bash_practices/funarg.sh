#!/bin/bash

fun () {
  echo "$1 is the first argument to fun()"
  echo "$2 is the second argument to fun()"
}

echo "$1 is the first argument to the script."
echo "$2 is the second argument to the script."

fun Yes 7
