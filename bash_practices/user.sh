#!/bin/bash

user=("john" 122 "sudo,developers" "bash")

echo "User Name: ${user[0]}"
echo "User ID: ${user[1]}"
echo "User Groups: ${user[2]}"
echo "User Shell: ${user[3]}"
