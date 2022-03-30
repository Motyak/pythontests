#!/bin/bash
for e in examples/*.in.txt; do
    echo $(basename $e .in.txt)
    diff -y $e ${e%in.txt}out.txt
    echo -e "\n"
done
