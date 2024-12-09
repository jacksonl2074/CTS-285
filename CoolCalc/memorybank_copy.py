# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 21:01:33 2024

@author: lkjac
"""

import csv

def read_file():
    with open('equations.csv', 'r', encoding='utf-8') as equations_file:
        equations = csv.reader(equations_file)
        for lines in equations:
            print(lines)
            
    return lines

def smth(lines):
    
    
    for row in lines:
        equation = row[0]  # Assuming each row contains one equation as a string
        correct_answer = row[1]  # Assuming the second column has the correct answer
        
        # Prompt the user for an answer
        user_answer = input(f"Solve the equation: {equation} = ")
        
        # Check if the user's answer is correct
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is {correct_answer}.")

lines = read_file()
smth(lines)
