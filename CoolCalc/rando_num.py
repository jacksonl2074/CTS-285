# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 21:14:45 2024

@author: lkjac
"""

import random
def random_number():
    '''
    This function generates a (pseudo) random number and asks user to 
    make a guess. Program tells them if guess is too high or low, and 
    tell them the number of guesses it took them to answer correctly.

    Returns
    -------
    None.

    '''
    print("Welcome to Number Guesser!")
    
    random_integer = random.randint(1, 50)
    # print(random_integer)     #print statement only to see that code works
    num_guesses = 1         # number of guesses, initialized to 1 as user 
                            # starts with first guess
    user_guess = int(input("Guess a number between 1 and 50. I will tell you if "
                           "your guess is too high or too low. > "))


    try:
        # loop and decision structure to assess user's guess
        while user_guess != random_integer:
            
            # checks user input, guess must be between 1-50
            if user_guess < 1 or user_guess > 50:
                print("Guess must be between 1-50. Try again.")
                
            # evaluates user's input and tells user if guess is too high/low
            else:
                num_guesses += 1         # number of guesses increments by 1 for each guess
                if user_guess > random_integer:
                    print("Your guess is too high!")
                    
                elif user_guess < random_integer:
                    print("Your guess is too low!")
                    
                else:
                    print("Invalid.")
            
            user_guess = int(input("Guess again: >"))
            
        print(f"\nCongrats! You guessed the correct number: {random_integer}")
        # print(random_integer)
        print(f'You guessed the correct number in {num_guesses} guesses.\n')
        
    except:
        print("Error\n")
    
# random_number()