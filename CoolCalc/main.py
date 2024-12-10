# -*- coding: utf-8 -*-
"""
CTS-285
M3HW2 - Cool Calculator (Dataman)
Laura K. Jackson
12.10.2024

This program simulates a calculator for elementary-aged children. There is
an answer checker to perform math equations, memory bank to help children with
their most difficult problems, and the random number guesser for fun.
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
              

# call main()
if __name__ == "__main__":
  main()
