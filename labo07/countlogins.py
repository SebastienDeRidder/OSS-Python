#!/usr/bin/python3

import sys


# Dit script neemt auth.log logfiles als command line parameters om hierin te
# tellen hoe vaak door elke user is ingelogd en hoe vaak van elk IP adres is
# ingelogd. Op het einde worden deze aantallen geprint.

# Opdracht:
# Vervolledig dit script volgens de comments die beginnen met "TODO".

'''
Lines indicating successful logins:
Mar 19 08:59:16 bletchley sshd[183804]: Accepted password for s124134 from 91.177.112.120 port 50898 ssh2
Mar 31 15:06:52 bletchley sshd[224703]: Accepted publickey for dieter from 84.198.36.41 port 55042 ssh2: RSA SHA256:vRs4IXI4TVdoCbzjigjd7zKTBr6SLQzPVdKN04CLFjI
'''

def countlogins(log, by_user, by_ip):
    '''
    Count succesful logins by each user and from each IP adress in open
    logfile ``log'' and store the results in dictionaries ``by_user'' and
    ``by_ip''.
    '''
    for line in log:
        words = line.split()
        # Only process lines from sshd service:
        if len(words) < 5 or not words[4].startswith('sshd'):
            continue
        # Skip lines when the word after sshd[...] is not "Accepted"
        if words[5] != "Accepted":
            continue

        user = words[8] # The user is at index 8
        by_user.setdefault(user, 0) # Add user to by_user dict if not exists
        by_user[user] += 1

        # Add code for by_ip
        ip_address = words[10] # The IP address is at index 10
        by_ip.setdefault(ip_address, 0) # Add IP address to by_ip dict if not exists
        by_ip[ip_address] += 1

logfiles = sys.argv[1:]
usercounts = {}
ipcounts = {}

for logfile in logfiles:
    try:
        with open(logfile, 'r') as f:
            countlogins(f, usercounts, ipcounts)
    except FileNotFoundError:
        print(f"Error: {logfile} not found.")
        continue

print("User counts:")
for user, count in usercounts.items():
    print(f"{user}: {count}")

print("IP counts:")
for ip, count in ipcounts.items():
    print(f"{ip}: {count}")
