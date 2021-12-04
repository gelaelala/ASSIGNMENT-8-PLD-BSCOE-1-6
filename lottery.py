#Program 1: Lottery
#Create a program that ask 3 numbers (0-9) from the user.
#Generate 3 random winning numbers (0-9)
#Display “Winner” if all 3 input numbers matched the generated numbers
#Display ”You loss” if not
#Display ”Try again y/n” after each game
#If the user enter “y” the user will play again
#if “n” the program will exit.

import random 
import time
from colorama import Fore, Back, Style

def programintro ():
    print (Fore.YELLOW + "Welcome to loterry!")
    time.sleep (2)
    print (Fore.RESET)
    print ("Please enter three numbers ranging from 0 to 9 and test your luck if the program will generate the same set of numbers as yours.")
    time.sleep (2)
    print ("Good luck!")

def getnumbers ():
    time.sleep (2)
    threenumbers = int(input("Enter three numbers here: "))
    return threenumbers

programintro ()

numbers = getnumbers ()