"""
Program name: Deal Cards
Author: Jean Lekefua Fombindia
Purpose: program that simulates dealing a hand of cards. 
The program will ask the user how many cards to deal and then generate that many random cards.
Date: February 10, 2026

"""
import random

def deal_cards():
    card_values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    suits = ["c", "h", "s", "d"]

    deck = []

    for value in card_values:
        for suit in suits:
            deck.append(value + suit)

    num_cards = int(input("How many cards would you like to be dealt? "))

    random.shuffle(deck)

    hand = []

    for i in range(num_cards):
        hand.append(deck[i])

    print("Your hand:")
    for card in hand:
        print(card)

    print("Total number of cards dealt:", num_cards)

deal_cards() 