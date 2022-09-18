#!/bin/bash
touch info.txt
echo "Hello, dear $(whoami)!" > info.txt
echo "date: $(date)" >> info.txt
echo "OS: $(uname)" >> info.txt
echo "home directory: $(pwd)" >> info.txt
used=$(df -h | awk 'NR==2{print $4}')
free=$(df -h | awk 'NR==2{print $5}')
echo "used memory = $used" >> info.txt
echo "free memory = $free" >> info.txt
dir=$(ls -la | grep ^d | wc |awk '{print$1}')
echo "folders = $dir" >> info.txt
files=$(ls -laR | grep ^- | wc |awk '{print$1}')
echo "files = $files" >> info.txt
