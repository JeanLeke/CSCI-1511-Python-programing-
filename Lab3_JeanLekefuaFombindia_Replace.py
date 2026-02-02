
"Program Name: Replace an item in List"
"Author: Jean Lekefua Fombindia"
"Purpose: The purpose of this is to replace one item with 'binoculars' and demonstrate slice notation."
"Date: February 3, 2026"

from Lab3_JeanLekefuaFombindia_add import packing_list

packing_list[5] = "binoculars"

index = packing_list.index("binoculars")

print(packing_list[:index])      
print(packing_list[index])       
print(packing_list[index + 1:]) 