#-----------------------------------------------------------------------------
# Name:        Math Functions (main.py)
# Purpose:     Calculate quadratic roots given coefficients using formula
#
# Author:      Darsh Gupta
# Created:     24-Mar-2026
# Updated:     24-Mar-2026
#-----------------------------------------------------------------------------
import math

# get coefficients from user
a = int(input("Enter coefficient a: "))
b = int(input("Enter coefficient b: "))
c = int(input("Enter coefficient c: "))

# determine if real roots exist, if they do calculate and print numerically
if (b ** 2 - 4*a*c) < 0:
  print("No Real Roots")
else:
  root_one = round((-b + math.sqrt(b ** 2 - 4*a*c))/(2*a), 1)
  root_two = round((-b - math.sqrt(b ** 2 - 4*a*c))/(2*a), 1)
  
  if root_one < root_two:
    print("Root:", root_one)
    print("Root:", root_two)
  elif root_one == root_two:
    print("Root:", root_one)
  else:
    print("Root:", root_two)
    print("Root:", root_one)