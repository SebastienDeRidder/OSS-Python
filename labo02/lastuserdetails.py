#!/usr/bin/python3

# read contents of file
ff = open('/etc/passwd', 'r')
data = ff.read()
ff.close()
lines = data.split('\n')
last = lines[-2]
print(last)
values = last.split(':')
print('Gebruikersnaam: ', values[0])
print('userid: ', values[2])
print('home directory: ', values[-1])