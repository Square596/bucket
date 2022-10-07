#!/bin/bash
path=$HOME/info.txt
echo "Hello, dear $(whoami)!" > $path
echo "date: $(date)" >> $path
echo "OS: $(uname)" >> $path
echo "home directory: $HOME" >> $path

used=$(df $HOME -h | awk "NR==2{print $4}")
free=$(df /c -h | awk "NR==2{print $5}")
echo "used memory = $used" >> $path
echo "free memory = $free" >> $path

dir=$(ls $HOME -la | grep ^d | wc |awk '{print$1}')
echo "folders = $dir" >> $path

files=$(find $HOME -maxdepth 1 -type f | wc -l)
echo "files = $files" >> $path

