#!/usr/bin/env python

while True:
    try:
        num1 = float(input("Geef het eerste getal: "))
        num2 = float(input("Geef het tweede getal: "))
        operator = input("Geef de bewerking (+, -, *, /): ")
        
        if operator == '+':
            result = num1 + num2
            print(f"Het resultaat is: {result}")
            break
        elif operator == '-':
            result = num1 - num2
            print(f"Het resultaat is: {result}")
            break
        elif operator == '*':
            result = num1 * num2
            print(f"Het resultaat is: {result}")
            break
        elif operator == '/':
            if num2 == 0:
                print("Fout: delen door nul is niet toegestaan")
            else:
                result = num1 / num2
                print(f"Het resultaat is: {result}")
                break
        else:
            print("Fout: ongeldige bewerking")
    except ValueError:
        print("Fout: ongeldig getal")
    except KeyboardInterrupt:
        print("\nProgramma afgebroken door gebruiker")
        break
