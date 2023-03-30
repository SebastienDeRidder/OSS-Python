#!/usr/bim/python3

import sys

data = sys.argv[1:]
line_number = 1

try:
    for filename in data:
        with open(filename, "r") as file:
            for line in file:
                formatted_line_number = str(line_number).zfill(6)
                print(f"{formatted_line_number}\t{line}", end="")
                line_number += 1

        print()

except FileNotFoundError:
    print("Er is een bestand niet gevonden. Controleer de opgegeven bestandsnamen en probeer het opnieuw.")

except Exception as e:
    print("Er is een onverwachte fout opgetreden:", e)
