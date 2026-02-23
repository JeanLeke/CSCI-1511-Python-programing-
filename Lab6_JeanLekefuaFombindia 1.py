"""
Program: User Login System
Author: Jean Lekefua Fombindia
Purpose: is to create a program that simulates a user login system using a 
dictionary to store usernames and passwords.
Date: 02/24/26

"""
users = {
    "Mike": "blueSky22",
    "John": "Sunshine7",
    "David": "Pass1234",
    "guest": "guest"
}
username = input("Enter username: ")

if username not in users:
    print("User not found. Exiting.")
else:
    password = input("Enter password: ")
    if password == users[username]:
        if username == "guest":
            print("Welcome,", username + ". You have Guest access.")
        else:
            print("Welcome,", username + ". You have Security Level 1.")
    else:
        print("Access Denied.")