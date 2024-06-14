#!/bin/bash

error () {
  blabla
  return 0
}

error
echo "The return status of the error function is: $?"
