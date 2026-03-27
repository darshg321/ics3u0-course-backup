#-----------------------------------------------------------------------------
# Name:        Functions (main.py)
# Purpose:     Convert miles to km, convert time to seconds, find letter 
#              count in a string
# Author:      Darsh Gupta
# Created:     24-Mar-2026
# Updated:     24-Mar-2026
#-----------------------------------------------------------------------------

def miles_to_km(miles):
  '''Convert Miles to Kilometers

  '''
  if miles < 0:
    return None
  else:
    return miles * 1.61

def time_in_seconds(minutes, seconds):
  '''Find time from minutes and seconds in only seconds

  '''
  if minutes < 0 or seconds < 0:
    return None
  else:
    return minutes * 60 + seconds

def letter_count(string_one, string_two):
  '''Determine how many times the second string appears in the first

  '''
  count = 0
  for char in string_one:
    if char == string_two:
      count += 1
  return count