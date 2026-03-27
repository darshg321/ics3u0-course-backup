#-----------------------------------------------------------------------------
# Name:        Strings (main.py)
# Purpose:     Check a user's password for a list of requirements, print
#              out a specific error message if it does not meet criteria.
# Author:      Darsh Gupta
# Created:     24-Mar-2026
# Updated:     24-Mar-2026
#-----------------------------------------------------------------------------

# get user password
password = input("Enter password: ")
is_valid = True

# run through a series of checks to determine if the password is valid, print specific error messages if not
if len(password) < 8:
  print("Error: Password must be at least 8 characters long.")
  is_valid = False

if password.isupper():
  print("Error: Password must contain at least one lowercase letter.")
  is_valid = False

if password.swapcase().isupper():
  print("Error: Password must contain at least one uppercase letter.")
  is_valid = False

has_digit = False
for char in password:
  if char.isdigit():
    if has_digit == True:
      print("Error: Password must contain exactly one digit.")
      is_valid = False
      break
    has_digit = True

if has_digit == False:
  print("Error: Password must contain exactly one digit.")
  is_valid = False

if is_valid == True:
  print("Password is valid.")
