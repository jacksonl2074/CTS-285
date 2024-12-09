# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 20:22:30 2024

@author: lkjac
"""



def read_file():
    with open('equations.csv', 'r', encoding='utf-8') as equations:
    
        for line in equations:
            print(line.rstrip())
    
        
    
read_file()