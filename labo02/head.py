#!/usr/bin/python3

import sys

data = sys.argv[1:]

for filename in data:
    with open(filename, "r") as file:
        for i in range(10):
            line = file.readline()
            if not line:
                break
            print(line, end="")
    print('\n')