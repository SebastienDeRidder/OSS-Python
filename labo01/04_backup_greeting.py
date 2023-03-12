#!/usr/bin/python3

# read contents of file
ff = open('greeting,txt', 'r')
lines = ff.read()
ff.close()

# write contents of greeting.txt to backup file
ff = open('greeting_backup,txt', 'w')
ff.write(lines)
ff.close()