"Program name: is Restaurant tip calculator"
"Author: Jean lekefua Fombindia"
"Purpose: the purpose of this program is to calculate the 15% and 20% tip suggestion and dispplays the tip amount"
"Starter code: None"
"Date: January 26th 2026"
 
total_bill = float(input("Enter the total bill amount: $"))

tip_15 = total_bill * 0.15
tip_20 = total_bill * 0.20

total_with_15 = total_bill + tip_15
total_with_20 = total_bill + tip_20

print(f"15% Tip: ${tip_15:.2f}")
print(f"20% Tip: ${tip_20:.2f}")

print(f"Total with 15% Tip: ${total_with_15:.2f}")
print(f"Total with 20% Tip: ${total_with_20:.2f}")