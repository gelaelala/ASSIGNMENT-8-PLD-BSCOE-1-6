#Program 2: Guess the number
#Generate 1 random number (0-100)
#Ask the user to guess the number
#Display “Greater than” if the inputed number is greater than the random number
#Display “Less than” if the inputed number is less than the random number
#Repeat asking the user until the random number has been guessed correctly.

import random
import time
import sys
from colorama import Fore, Back, Style


def programintro ():
    print ("Hello and welcome to 'Guess the Number'!")
    time.sleep (1.5)
    print ("All you have to do is to guess the number which was randomly generated by the game.")
    time.sleep (1.5)
    print ("Don't worry we'll give you hints on whether the number that you guessed is higher or lower than the number generated.")
    time.sleep (1.5)
    print ("That's all, good luck player!")
    time.sleep (2)

def enternumber ():
    print ("The program has successfully generated a number! It's your turn to guess it!")
    time.sleep (2)
    guesses = 0
    answer = random.randint (0, 100)
    while True:
        guesses += 1
        userinput = int(input("Enter your guess here: "))
        if userinput > answer:
            print (Fore.YELLOW + "The number you've guessed is greater than the generated number. Please try again.")
            print (Fore.RESET)
            time.sleep (1.5)
        elif userinput < answer:
            print (Fore.BLUE + "The number you've guessed is less than the generated number. Please try again.")  
            print (Fore.RESET)
            time.sleep (1.5)
        elif userinput == answer:
            break
    if userinput == answer:
        if guesses == 1:
            print (Fore.GREEN + "Congratulations! You guessed the correct number!")
            print (Fore.RESET)
            time.sleep (2)
            print (f"The number generated by the game is {answer} and you've guessed it for {guesses} time.")
            time.sleep (2)
            print ("That's all, I hope you enjoyed this game.")
            time.sleep (2)
            print ("Thank you for playing and I hope to see you again!")
            time.sleep (2)
            sys.exit
        elif guesses > 1:
            print (Fore.GREEN + "Congratulations! You guessed the correct number!")
            print (Fore.RESET)
            time.sleep (2)
            print (f"The number generated by the game is {answer} and you've guessed it for {guesses} times.")
            time.sleep (2)
            print ("That's all, I hope you enjoyed this game.")
            time.sleep (2)
            print ("Thank you for playing and I hope to see you again!")
            time.sleep (2)
            sys.exit

programintro ()

enternumber ()