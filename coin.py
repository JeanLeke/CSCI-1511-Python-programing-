"""
Program: Match Coins Game
Author: Jean Lekefua Fombindia
Purpose: This file defines the Coin class which represents a tossable coin.
Date: 23 March 2026
"""

import random

class Coin:
    def __init__(self):
        self.__sideup = "Heads"

    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"

    def get_sideup(self):
        return self.__sideup