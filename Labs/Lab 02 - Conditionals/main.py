#-----------------------------------------------------------------------------
# Name:        Conditionals (main.py)
# Purpose:     Give the user their achievement level based on their grade.
#
# Author:      Darsh Gupta
# Created:     4-Feb-2026
# Updated:     4-Feb-2026
#-----------------------------------------------------------------------------

# get user's grade
grade = int(input("What is your grade? "))

# print the achievement level based on the user's grade
if grade > 100 or grade < 0:
  print("Invalid Grade.")
elif grade >= 80:
  print("Exceeding Expectations.")
elif grade >= 70:
  print("Meeting Expectations.")
elif grade >= 50:
  print("Needs Improvement.")
else:
  print("Not Passing.")
