"""
Write a program that does the following:
Asks the user to enter in 2 numbers that can be float values
Ask the user if one of the numbers is the hypotenuse of a right triangle
Calculates the length of the missing side and rounds it to 1 decimal place.
"""
import math
x=input("Enter a number:")
#convert to a number
x=float(x)
y=input("Enter a number:")
#convert to a number
y=float(x)
p=input("Is one of the numbers the hypotnuse?Yes or No?:")

if p =="Yes" or "yes":
   b=pow(x,2)-pow(y,2)
   c=math.sqrt(b)
   print(c)
elif p=="No" or "no":
   d=pow(x,2)+pow(y,2)
   h= math.sqrt(d)
   print(h)


