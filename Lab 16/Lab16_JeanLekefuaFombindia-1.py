# Lab16_username-1.py

"""
Program Name: Ohio Unemployment Plot
Author: Jean Lekefua Fombindia
Purpose: A program that reads the OHRU.csv file, 
which contains Ohio's unemployment rate since 1976
Date: 05/11/2026
"""

import csv
import datetime
import matplotlib.pyplot as plt


Dates = []
Rates = []

with open("OHUR.csv", "r") as file:
    reader = csv.reader(file)

    header = next(reader)

    print("Header Columns:")
    for index, column in enumerate(header):
        print(index, column)

    for row in reader:
        try:
            date = datetime.datetime.strptime(row[0], "%Y-%m-%d")
            rate = float(row[1])

            Dates.append(date)
            Rates.append(rate)

        except ValueError:
            print("Error reading row:", row)

plt.plot(Dates, Rates)

plt.title("Ohio Unemployment (by Month): 1976 - 2022")
plt.xlabel("Date")
plt.ylabel("Unemp Rate")

plt.xticks(rotation=45)

plt.savefig("ohio_unemployment.png")

plt.show()

print("Plot saved as ohio_unemployment.png")
