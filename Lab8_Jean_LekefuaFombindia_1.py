"""
Program Name: UPC Validator
Author: Jean Lekefua Fombindia
Purpose: This program is to checks whether a 12-digit UPC-A code is valid by
calculating the correct check digit and comparing it to the last digit entered.
Date: March 10, 2026
"""


def find_UPC(first11):

    odd_sum = 0
    even_sum = 0

    for i in range(len(first11)):
        digit = int(first11[i])

        if i % 2 == 0:
            odd_sum += digit
        else:
            even_sum += digit

    total = (odd_sum * 3) + even_sum
    check_digit = (10 - (total % 10)) % 10

    return check_digit


def main():

    upc = input("Enter a 12-digit UPC: ")

    if len(upc) != 12 or not upc.isdigit():
        print("Invalid input. UPC must contain exactly 12 digits.")
        return

    first11 = upc[:11]
    provided_digit = int(upc[11])

    print("\nThe first 11 digits are:", first11)
    print("The provided check digit is:", provided_digit)

    print("\nCalculating...")

    expected_digit = find_UPC(first11)

    print("The expected check digit is", expected_digit)

    if expected_digit == provided_digit:
        print("\nThis is a VALID UPC.")
    else:
        print("\nThis is an INVALID UPC.")


main()