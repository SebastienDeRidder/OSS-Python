#!/usr/bin/env python

## sudo apt install python3-pip
## pip install termcolor

import sys
from termcolor import colored # module voor het printen in kleur


zoekpatroon = sys.argv[1]
bestandsnaam = sys.argv[2]

with open(bestandsnaam) as bestand:
    for regel in bestand:
        if zoekpatroon in regel:
                print(colored(regel.replace(zoekpatroon, colored(zoekpatroon, 'red')), 'white'), end="")