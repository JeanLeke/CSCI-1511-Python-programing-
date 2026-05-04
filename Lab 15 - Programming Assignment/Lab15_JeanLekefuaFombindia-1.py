"""
Program Name: Plot a math Formula
Author: Jean Lekefua Fombindia
Purpose: Is to Write a program that uses matplotlib to plot math formulas.
Date: 05/04/2026
"""

import matplotlib.pyplot as plt
import math

x = []
y = []

for i in range(0, 361):
    x.append(i)
    y.append(math.sin(math.radians(3 * i)))

plt.plot(x, y)

plt.title("Multiple Sine Graph")
plt.xlabel("X (degrees)")
plt.ylabel("Y")

plt.grid()

plt.savefig("my_plot.png")

plt.show() 