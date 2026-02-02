
"Program Name: Add to a list"
"Author: Jean Lekefua Fombindia"
"Purpose: Is to import the packing list, and add more items to the list, also printing the list in reverse order"
"Date: February 3, 2026"

from Lab3_JeanLekefuaFombindia_list import packing_list

packing_list.append("knife")
packing_list.append("toothbrush")
packing_list.append("extra clothes")
packing_list.append("power bank")
packing_list.append("raincoat")

print(sorted(packing_list, reverse=True)) 