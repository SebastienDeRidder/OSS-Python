#!/usr/bin/python3

import subprocess

# Get list of valid login shells
with open('/etc/shells', 'r') as shells_file:
    valid_shells = [line.strip() for line in shells_file]

# Get list of human users from /etc/passwd
with open('/etc/passwd', 'r') as passwd_file:
    human_users = [line.split(':')[0] for line in passwd_file if line.split(':')[6].strip() in valid_shells]

# Get list of users who have logged in since cutoff date
last_output = subprocess.check_output(['last', '--since', '-1month'])
recent_users = [line.split()[0] for line in last_output.decode('utf-8').split('\n') if line and line.split()[0] in human_users]

# Get list of inactive users
inactive_users = list(set(human_users) - set(recent_users))

# Print list of inactive users
print("Inactive users:")
for user in inactive_users:
    print