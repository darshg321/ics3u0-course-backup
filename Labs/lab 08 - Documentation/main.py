#-----------------------------------------------------------------------------
# Name:        Documentation (Calling Functions) (main.py)
# Purpose:     Documenting delivery game code
#
# Author:      Darsh Gupta
# Created:     20-Apr-2026
# Updated:     26-Mar-2026
#-----------------------------------------------------------------------------

import random

def miles_to_km(miles):
  '''
  Converts miles to kilometers
  
  Takes in miles as a parameter, returns None if negative, otherwise 
  converts it to kilometers and returns the output

  Parameters
  ----------
  parameter1 : int/float
    number of miles to convert to kilometers
  
  Returns
  -------
  int/float
    number of kilometers
  '''
  if miles < 0:
    return None
  return miles * 1.61

def time_in_seconds(minutes, seconds):
  '''
  Converts combination of time to seconds
  
  Takes in minutes and seconds as a parameter, returns
  None if either are negative, otherwise converts it to 
  just seconds and returns the output

  Parameters
  ----------
  parameter1 : int/float
    number of minutes to convert to seconds
  parameter2 : int/float
    number of seconds to add to seconds
    
  Returns
  -------
  int/float
    number of seconds
  '''
  if minutes < 0 or seconds < 0:
    return None
  return minutes * 60 + seconds


# introduce the game
print("----Delivery Adventure!----")
print("Reach the destination in as few turns as possible.")
print("If you overshoot the distance, you restart.\n")

turns = 0
playing_game = True

while playing_game:
  # generate random delivery route and conditions
  total_miles = random.randint(5, 20)
  speed_mph = random.randint(20, 60)
  total_km = miles_to_km(total_miles)

  print(f"New Delivery Route: {round(total_km, 2)} km away")
  print(f"Vehicle Speed: {speed_mph} mph")

  remaining_distance = total_miles

  #
  while remaining_distance > 0:
    turns += 1
    print(f"\nTurn {turns}")
    print(f"Remaining Distance: {round(miles_to_km(remaining_distance), 2)} km")

    # get user's attempt
    guess_distance = float(input("How many miles will you travel this turn? "))
    minutes = int(input("Minutes you will drive: "))
    seconds = int(input("Seconds you will drive: "))

    km_guess = miles_to_km(guess_distance)
    total_time = time_in_seconds(minutes, seconds)

    # penalize user for invalid input
    if km_guess is None or total_time is None:
      print("Invalid values, turn penalty.")
      continue

    hours = total_time / 3600
    actual_distance = speed_mph * hours

    # random events
    if guess_distance < 2:
      print("Too slow... dog chase! Time penalty.")
      actual_distance *= 0.8

    elif guess_distance > 8:
      print("Too fast! Engine strain.")
      actual_distance *= 0.7

    elif 4 <= guess_distance <= 6:
      print("Optimal driving. Efficiency boost.")
      actual_distance *= 1.2

    print(f"You actually traveled {round(miles_to_km(actual_distance), 2)} km")

    # overshoot check
    if actual_distance > remaining_distance:
      print("\nYou overshot the destination! Restarting route...\n")
      break

    remaining_distance -= actual_distance

    if remaining_distance <= 0:
      print("\nDelivery completed successfully!")
      print(f"Total turns taken: {turns}")
      playing_game = False
    