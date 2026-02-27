#-----------------------------------------------------------------------------
# Name:        Basics (main.py)
# Purpose:     Learn basic programming skills such as variables, types, input, and output 
#
# Author:      Darsh Gupta
# Created:     27-Feb-2026
# Updated:     27-Feb-2026
#-----------------------------------------------------------------------------

# Gather information on the user
name = input("What is your name? ")
age = input("How old are you? ")
print(f"Hello {name}, you are currently {age} years old.")

# Give the user their future age
future_age = int(age) + 10
print(f"In 10 years, you will be {future_age} years old.")

# Get numbers to run tasks with
first_num = int(input("Enter a number: "))
second_num = int(input("Enter another number: "))

# Perform a variety of basic math operations and display them to the user
print(f"Sum: {first_num + second_num}")
print(f"Difference: {first_num - second_num}")
print(f"Product: {first_num * second_num}")
print(f"Quotient: {first_num / second_num}")
print(f"Integer Division: {first_num // second_num}")
print(f"Modulo: {first_num % second_num}")
print(f"Power: {first_num ** second_num}")