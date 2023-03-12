#!/usr/bin/python3

# read contents of file
ff = open('greeting,txt', 'r')
lines = ff.read()
ff.close()

print(lines)