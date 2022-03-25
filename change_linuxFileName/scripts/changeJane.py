#!/usr/bin/env python3
from fileinput import filename
import os
import sys
import subprocess

def changeName(filenames):
    with open(filenames, mode='r',encoding='UTF-8') as f:
        for filepath in f.readlines():
            new_filepath = filepath.replace("jane","jdoe")
            print("mv {} {}".format(filepath.strip(),new_filepath.strip()))
            os.system("mv {} {}".format(filepath.strip(),new_filepath.strip()))


if __name__ == "__main__":
    filenames = sys.argv[1]
    changeName(filenames)