'''
Authored by Travis William Duncan
NumberGuessingGame.py

================================= DESCRIPTION =================================
This is a number guessing game.
Script generates a pseudorandom integer between 1 and 100.
The user is asked to guess which number was selected.
===============================================================================
'''
# import modules
import os
from random import randint
import console_format as cf
import instructions as ins

# Initialize variables for a randomly selected integer and the maximum guesses allowed
value = randint(1, 100)
guess_limit = 5
guess_count = 0
too_high = False
too_low = False

# Clear the console of any text
cf.ClearScreen()

# Printing game title and instructions
ins.print_instructions(guess_limit)

# Execute game logic loop
while guess_count < guess_limit:
  """Game logic loop"""
  cf.ClearScreen()
  guess_count += 1
  if too_low == True or too_high == True:
    if too_low == True:
      print("\n\nThe correct number is HIGHER\n")
    else:
      print("\n\nThe correct number is LOWER\n")
  else:
    print("\n\n\n")
  print("Guess an integer between 1 and 100!")
  print(f"\n\n\t::::::::Guess {guess_count} of {guess_limit}::::::::")
  guess = int(input("\n\tYour guess: "))
  print("\n\n")
  if guess == value:
    cf.ClearScreen()
    print("\t  ****CONGRATULATIONS!****  ")
    print("\n\t  You guessed correctly!  YOU WIN!!!")
    print(f"\n\t  The correct number was:  {value}")
    print(f"\n\t  You used {guess_count} guesses.")
    break
  else:
    if guess < value:
      too_low = True
      too_high = False
    else:
      too_high = True
      too_low = False
else:
  print(f"\n\n\t  Sorry!  You've used all {guess_limit} of your guesses.")
  print(f"\n\n\t  The correct number was:  {value}")
  print("\n\n\t\t\t  GAME OVER  \n\n\n\n")

# fin
