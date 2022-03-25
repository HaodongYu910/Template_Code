#!/bin/bash

>oldFiles.txt
doc_name=$(grep " jane " /home/student-00-94e743125e81/data/list.txt | cut -d " " -f 3)
for file in $doc_name; do
    if [ -f "/home/student-00-94e743125e81$file" ]; then
        echo "/home/student-00-94e743125e81$file" >> oldFiles.txt
    fi
done
