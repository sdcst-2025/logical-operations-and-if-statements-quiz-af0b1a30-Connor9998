#!python3
"""
Debug this program so that it runs

original code:
x = input("enter a decimal number"))
xi = int(x)
if (x - xi) == 0:
    print(f"{x} is an integer")
"""
x = input("enter a decimal number")
#convert to a number
x=float(x)
b=round(x,1)
if x - round(x,1)==0:
    print(f"{b} is an integer")
elif x != int():
    print(f"{x} is not an integer")