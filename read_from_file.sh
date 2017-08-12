#!/bin/bash

# create input files
# touch test/{1..5}.txt



# example1
# input="input.txt"
# while IFS= read -r var
# do
#   echo "$var"
# done < "$input"


# example2
# file="input.txt"
# while IFS= read -r line
# do
#         # display $line or do somthing with $line
# 	printf '%s\n' "$line"
# done <"$file"

# example 3
IFS=$'\n';for line in `cat input.txt`; do rm ${line} ; done
