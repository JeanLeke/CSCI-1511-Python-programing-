"Program Name: Remove an item from List"
"Author: Jean Lekefua Fombindia"
"Purpose: is to remove binoculars from the list and display the final list and total number of items"
"Date: February 3, 2026"

from Lab3_JeanLekefuaFombindia_Replace import packing_list

packing_list.remove("binoculars")

print(packing_list)

print(f"There are {len(packing_list)} total items being brought on the camping trip.")