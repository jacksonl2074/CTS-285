# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 19:01:22 2024

@author: lkjac
"""
# import modules
import answerchecker as ac
import memorybank as mb
import rando_num as rn

# constants
ANSWER = 1
MEMORY = 2
GUESSER = 3
EXIT = 4

def options_menu():
    '''
    Function displays the main menu to user with options for using
    calculator

    '''
    print("***Welcome to Cool Calculator!***\n")
    print("1. Answer Checker")
    print("2. Memory Bank")
    print("3. Number Guesser")
    print("4. Exit\n")
    

    
def main():
    '''
    Main function calls the menu to present list of calculator options 
    to user. Once user chooses an option, the correct function(s) is selected. 
    


    '''
    choice = 0
    
    while choice != EXIT:
        # try block to pull up menu and let user enter a choice
        try:
            options_menu()      # call menu for user to choose options
            
            choice = int(input("Enter your choice: "))
        
            # decision structure based on user input
            if choice == ANSWER:
                # call these functions/module
                ac.answer_checker()
                
            elif choice == MEMORY:
                # call these functions/module
                lines = mb.read_file()
                mb.present_equations(lines)
                
            elif choice == GUESSER:
                # call these functions/module
                rn.random_number()
                
            elif choice == EXIT:
                print("\nGoodbye! :) Come again soon!\n")
                
            else:
                print("Invalid input. Please try again.\n")
                
        # exception block for invalid entry
        except ValueError:
              print("Invalid input! Please enter a valid option.\n")
              
# may not use
def user_menu():
    print("Welcome to Cool Calculator!")
    print("Are you a student or parent?")
    print("1. Student")
    print("2. Parent/n")

# call main()
if __name__ == "__main__":
  main()
