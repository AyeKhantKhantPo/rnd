#!/bin/bash

if [ $(whoami) == 'root' ]; then
    echo "You are root"
else
    echo "You are not root"
fi
