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
import sys
from colorama import Fore, Back, Style

def programintro ():
    print (Fore.YELLOW + "Welcome to loterry!")
    time.sleep (2)
    print (Fore.RESET)
    print ("Please enter three numbers ranging from 0 to 9 and test your luck if the program will generate the same set of numbers as yours.")
    time.sleep (2)
    print ("Good luck!")

def getrandom ():
    lottonumbers = list()
    randomnumbers = sorted(random.sample (range (0,9), 3))
    lottonumbers.append (randomnumbers)
    return lottonumbers

def usernum ():
    number = 1
    userinput = []
    while number <= 3:
        usernum = int(input("Enter number here: "))
        time.sleep (2)
        userinput.append (usernum)
        number +=1
    return sorted (userinput)

def lotterytime (user, randomnumbers):
        print (Fore.CYAN + f"Your three numbers are {user}.")
        print (Fore.RESET)
        time.sleep(2)
        if user == randomnumbers:
            print (Fore.YELLOW + "Winner!")
            time.sleep (2)
            print ("Congratulations! You win the lottery!")
            time.sleep (2)
            print (Fore.RESET)
            print ("Thank you for playing and we hope to see you again!")
            sys.exit
        else:
                print (Fore.RED + "You loss.")
                print (Fore.RESET)
                time.sleep (2)
                print ("Sorry, you loss the game.")
                time.sleep (2)
                print (f"The numbers that you entered are {user} while the numbers generated by the program are {randomnumbers}.")
                time.sleep (2)
                question2 = input("Would you like to try again? (y/n): ")
                time.sleep (3)
                if question2 == "y":
                    print ("Restarting the game. Please wait.")
                    time.sleep (5)
                    print (Fore. RESET)
                    main ()
                elif question2 == 'n':
                    print (Fore.YELLOW + "That's all, thank you for playing the loterry. See you next time!")
                    print (Fore.RESET)
                    sys.exit

def main ():
    programintro ()
    randomnum = getrandom ()
    input = usernum ()
    lotterytime (input, randomnum)

main ()

