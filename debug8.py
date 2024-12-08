#!python3
"""
Debug this program so that it runs

original code:
x = input("enter a decimal number"))
xi = int(x)
if (x - xi) == 0:
    print(f"{x} is an integer")
"""

import math

x = input("Enter a decimal number:")
#convert to a number
x = float(x)
xi = int(x)
    
if x - xi == 0:
    print(f"{x} is an integer")
else:
    print(f"{x} is not an integer")
