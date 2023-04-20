#!/usr/bin/env python3

import os

# Maak een dictionary om de groepen in op te slaan
groups = {}

# Lees /etc/group en sla de groepen op in de dictionary
with open('/etc/group', 'r') as f:
    for line in f:
        # split de regel in velden
        fields = line.strip().split(':')
        # de derde kolom bevat een komma-gescheiden lijst van gebruikers
        users = fields[3].split(',')
        # maak een set van gebruikers
        user_set = set(users)
        # sla de set op in de dictionary onder de groepsnaam
        groups[fields[0]] = user_set

# Lees /etc/passwd en voeg de primary group van elke gebruiker toe aan de set voor die groep
with open('/etc/passwd', 'r') as f:
    for line in f:
        fields = line.strip().split(':')
        # de vierde kolom bevat de GID van de primary group van de gebruiker
        gid = fields[3]
        # voeg de gebruiker toe aan de set van de bijbehorende groep
        if gid in groups:
            groups[gid].add(fields[0])

# Print alle groepen waar geen gebruikers in zitten
for group, users in groups.items():
    if len(users) == 0:
        print(group)