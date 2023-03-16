#!/usr/bin/env python

import sys

if len(sys.argv) <= 2:
    start = 0
    end = int(sys.argv[1])
else:
    start = int(sys.argv[1])
    end = int(sys.argv[2])

while start <= end:
    print(start)
    start += 1