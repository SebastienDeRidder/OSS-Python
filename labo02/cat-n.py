#!/usr/bim/python3

import sys

data = sys.argv[1:]
line_number = 1

for filename in data:
    with open(filename, "r") as file:
        for line in file:
            formatted_line_number = str(line_number).zfill(6)
            print(f"{formatted_line_number}\t{line}", end="")
            line_number += 1

    print()