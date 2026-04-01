"""
Program Name: Word Count
Author: Jean Lekefua Fombindia
Purpose: This program is to create an OOP-based program that displays a menu of 4 predefined 
text files, lets the user choose one, then reads and analyzes that file. The program will count the 
frequency of every word in the selected file and print an alphabetical report.
Date: March 31, 2026

"""

from pathlib import Path
import string

class WordAnalyzer:

    def __init__(self, file_name):
        self.file = Path(file_name)   
        self.counts = {}             

    def process_file(self):

        if not self.file.exists():
            return False

        try:
            with open(self.file, "r") as f:

                for line in f:

                    line = line.lower()  

                    for char in string.punctuation:
                        line = line.replace(char,"")

                    words = line.split() 

                    for word in words:
                        if word in self.counts:
                            self.counts[word] += 1
                        else:
                            self.counts[word] = 1
            return True

        except:
            return False

    def print_report(self):
        print("\n--- Results ---\n")

        for word in sorted(self.counts):
            print(word, "-", self.counts[word])


def main():

    while True:
        print("\nWord Analyzer Menu")
        print("1. Princess Mars")
        print("2. Tarzan")
        print("3. Treasure Island")
        print("4. Monte Cristo")
        print("5. Exit")

        user_choice = input("Choose a file (1-5): ")

        if user_choice == "5":
            print("Exiting program...")
            break

        if user_choice == "1":
            file_name = "princess_mars.txt"
        elif user_choice == "2":
            file_name = "Tarzan.txt"
        elif user_choice == "3":
            file_name = "treasure_island.txt"
        elif user_choice == "4":
            file_name = "monte_cristo.txt"
        else:
            print("Invalid option, try again.")
            continue

        analyzer = WordAnalyzer(file_name)

        if analyzer.process_file():
            analyzer.print_report()
        else:
            print("Could not open file.")

        input("\nPress Enter to go back to menu...")


main() 