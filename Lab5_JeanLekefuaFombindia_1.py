"""
Prgram Name: Dice Rolling Terms
Author: Jean Lekefua Fombindia
Purpose: Is to Write a program that rolls two dice, prints the outcome, 
and then uses conditional statements to print the appropriate term for that roll based
Date: 02/17/2026
"""

import random

while True:
   
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2

    print(f"\nDie 1: {die1}")
    print(f"Die 2: {die2}")
    print(f"Total: {total}")

    if die1 == 1 and die2 == 1:
        term = "Snake Eyes"

    elif (die1 == 1 and die2 == 2) or (die1 == 2 and die2 == 1):
        term = "Ace Caught a Deuce"

    elif die1 == 2 and die2 == 2:
        term = "Little Joe from Kokomo"

    elif (die1 == 1 and die2 == 4) or (die1 == 4 and die2 == 1):
        term = "Little Phoebe"

    elif (die1 == 2 and die2 == 3) or (die1 == 3 and die2 == 2):
        term = "Little Phoebe"

    elif die1 == 3 and die2 == 3:
        term = "Jimmy Hicks from the Sticks"

    elif (die1 == 6 and die2 == 1) or (die1 == 1 and die2 == 6):
        term = "Six Ace"

    elif die1 == 4 and die2 == 4:
        term = "Eighter from Decatur"

    elif (die1 == 3 and die2 == 6) or (die1 == 6 and die2 == 3):
        term = "Nina from Pasadena"

    elif (die1 == 4 and die2 == 5) or (die1 == 5 and die2 == 4):
        term = "Nina from Pasadena"

    elif die1 == 5 and die2 == 5:
        term = "Puppy Paws"

    elif (die1 == 6 and die2 == 5) or (die1 == 5 and die2 == 6):
        term = "Six Five no Jive"

    elif die1 == 6 and die2 == 6:
        term = "Boxcars"
    else:
        term = "No special term"

    print (term)
    
    print("Thanks for playing!")
    break
