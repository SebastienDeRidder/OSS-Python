#!/usr/bin/python3

import sys

data = sys.argv[1:]
for filename in data:
    with open(filename, "r") as file:
        content = file.read()
        print(content)
    print()