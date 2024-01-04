'''
Program name: ConsoleFormat.py
Author: Travis William Duncan

Purpose:  The ConsoleFormat module contains functions used to
quickly and easily introduce formatting to the onscreen console
'''

# Importing 'os' module
import os
from termcolor import colored

# Defining function to clear screen:
def ClearScreen():
    """This function clears the console of any onscreen characters.
    It checks whether the program is running in
    a Linux / iOS operating system.
    For Linux / iOS, the os.system('clear') command is used.

    Otherwise, it is assumed that the program is running in Windows
    and the os.system('cls') command is used.
    """
    command = 0
    # If os.name is 'posix', the Linux / iOS command will be used
    if os.name == 'posix':
        command = os.system('clear')
    # Otherwise, the Windows command will be used
    else:
        command = os.system('cls')


# Defining function to insert an empty line to console
# Arguments can be provided to insert a string
# and specify a color for the string
def Lines(i=1, message='', b=0, color=''):
    if i != 0:
        EmptyLines = '\n' * i
        print(EmptyLines)
    if message != '':
        print(colored(message, color))
    if b != 0:
        EmptyLines = '\n' * b
        print(EmptyLines)

# Defining function to print a thick bar to console
def ThickBar():
    print("=" * 75)

# Defining function to print a thin bar to console
def ThinBar():
    print("-" * 75)

def MenuTitle(Title, Message):
    cf.ClearScreen()
    print(f" === {Title} ===")
    cf.EmptyLine()
    Message(ContactsList)
    cf.EmptyLine()