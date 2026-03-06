#-----------------------------------------------------------------------------
# Name:        Repetition (main.py)
# Purpose:     find the series sum between two numbers, then find the largest
#              factor of a number
# Author:      Darsh Gupta
# Created:     3-Mar-2026
# Updated:     3-Mar-2026
#-----------------------------------------------------------------------------

# TASK 1
# get user's number
firstNumber = int(input("Input the first number of your series: "))
secondNumber = int(input("Input the second number of your series: "))

# find the series sum between both numbers, inclusive
sum = 0
if firstNumber > secondNumber:
  print("Invalid")
else:
  for n in range(firstNumber, secondNumber+1): # add one to max, because range() is exclusive
    sum += n
  print("Sum: ", sum)

# TASK 2
# get user's factor number as int
factorNumber = int(input("Input a number to find the largest factor: "))

# try the largest factor as number-1, continue decrementing until divison results in an integer, give user answer
largest_factor = factorNumber-1
while (not ((factorNumber / largest_factor).is_integer())):
  largest_factor -= 1
  
if largest_factor == 1:
  print("Prime")
else:
  print("Largest Factor: ", largest_factor)
  
