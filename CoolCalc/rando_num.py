# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 21:14:45 2024

@author: lkjac
"""

import random
def random_number():
    
    random_integer = random.randint(1, 50)
    print(random_integer)     #print statement only to see that code works
    user_guess = int(input("Guess a number between 1 and 50. I will tell you if "
                           "your guess is too high or too low. > "))
    
    # loop and decision structure to assess user's guess
    while user_guess != random_integer:
        if user_guess > random_integer:
            print("Your guess is too high!")
            
        elif user_guess < random_integer:
            print("Your guess is too low!")
    
        else:
            print("Invalid")
            
        user_guess = int(input("Guess again: >"))
    print("\nCongrats! You guessed the correct number!")
    print(random_integer)
    
random_number()