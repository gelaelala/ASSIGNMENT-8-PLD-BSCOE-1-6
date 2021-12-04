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
    firstnumber = int(input("Enter first number here: "))
    time.sleep (1)
    secondnumber = int(input("Enter second number here: "))
    time.sleep (1)
    thirdnumber = int(input("Enter third number here: "))
    time.sleep (1)
    threenumbers = firstnumber, secondnumber, thirdnumber
    return threenumbers

def finalizing (threenumbers_):
    print (Fore.CYAN + f"Your three numbers are {threenumbers_}.")
    print (Fore.RESET)
    time.sleep (2)
    question = input("Are you sure with these numbers? (yes/no): ")
    if question == "yes":
        return threenumbers_
    else:
        getnumbers ()

def lotterytime (threenumbers):
    randomnumbers = random.randint (range (0,9), 3)
    for t in threenumbers:
        for r in randomnumbers:
            if t == r:
                print (Fore.YELLOW + "Winner!")
                time.sleep (2)
                print ("Congratulations! You win the lottery!")
                time.sleep (2)
                print 

programintro ()

threenumbers = getnumbers ()

finalizing (threenumbers)

lotterytime (threenumbers)