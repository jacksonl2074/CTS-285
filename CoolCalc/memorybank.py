# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 21:34:53 2024

@author: lkjac
"""

import csv

def read_file():
    '''
    This function reads a CSV of 4 math equations that student is having
    trouble with; passes the file's contents (in the form of a list) to the
    next function.

    Returns
    -------
    lines : string list of equations

    '''
    with open('equations.csv', 'r', encoding='utf-8') as equations_file:
        equations = csv.reader(equations_file)
        lines = list(equations)  # Convert the reader object to a list
    return lines

def present_equations(lines):
    '''
    This function accepts the CSV file's contents (list of equations) and
    presents them for student to answer. Student is told whether each answer
    is correct or not.

    Parameters
    ----------
    lines : string list of equations

    Returns
    -------
    None.

    '''
    num_correct = 0         # number of correct answers, initialized to 0
    
    for row in lines:
        equation = row[0]  # Assuming each row contains one equation as a string
        correct_answer = row[1]  # Assuming the second column has the correct answer
        
        # Prompt the user for an answer
        user_answer = input(f"Solve the equation: {equation} = ")
        
        
        
        # Check if the user's answer is correct
        if user_answer == correct_answer:
            print("Correct!\n")
            num_correct += 1
        else:
            print(f"Incorrect. The correct answer is {correct_answer}.\n")
        
    print(f'You answered {num_correct} equations correctly.')
    print('Keep up the hard work!\n')
    # FIXME: add a run again? menu or questions

# Read the file and get the equations
# lines = read_file()

# Present the equations to the user
# present_equations(lines)
