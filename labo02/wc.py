#!/usr/bin/python3

import sys

# Lijsten om het totaal aantal lijnen, woorden en karakters bij te houden
total_lines = 0
total_words = 0
total_chars = 0


# print hoofding
print(f"{'Lijnen':>8s} {'Woorden':>8s} {'Karakters':>8s} {'Bestandsnaam':s}")
print("-" * 40)

# Loop door alle argumenten en verwerk elk bestand
for filename in sys.argv[1:]:
    # Variabelen om het aantal lijnen, woorden en karakters bij te houden voor dit bestand
    num_lines = 0
    num_words = 0
    num_chars = 0

    # Open het bestand en lees het in
    with open(filename, "r") as file:
        # Loop door alle lijnen van het bestand
        for line in file:
            # Tellen het aantal lijnen
            num_lines += 1

            # Tellen het aantal woorden
            num_words += len(line.split())

            # Tellen het aantal karakters
            num_chars += len(line)

    # Print de resultaten voor dit bestand
    print(f"{num_lines:8d} {num_words:8d} {num_chars:8d} {filename}")

    # Update de totale tellingen
    total_lines += num_lines
    total_words += num_words
    total_chars += num_chars

# Print de totalen
print(f"{total_lines:8d} {total_words:8d} {total_chars:8d} total")