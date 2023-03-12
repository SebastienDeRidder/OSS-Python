#!/usr/bin/python3

import sys

data = sys.argv[1:]

for filename in data:
    with open(filename, "r") as file:
        lines = file.readlines()
        for line in lines[-10:]:
            print(line, end="")
    print('\n')