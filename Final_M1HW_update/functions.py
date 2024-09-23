"""
CTS 285
M1HW - Calculator
Laura K. Jackson
9/2/2024
"""
# functions for each choice in calculator
import mathfunctions as mf

def get_numbers():
    '''
    Function takes user input for 2 numbers, num1 and num2, and returns
    them

    Returns
    -------
    num1 : int.
    num2 : int.

    '''
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    return num1, num2

def add():
  """
  Function adds 2 numbers that the user inputs
  Calls function to do the math and another to repeat the function
  """
# Chat GPT Prompt: how an i get this python code to run the addition function again  
# when user enter's 2 (repeat the # function)?
  try:
    user_choice = 1  # Initialize to 1 to enter the loop

    while user_choice == 1:
      print("Add")

      # call get_numbers() function
      num1, num2 = get_numbers()
      
      # call calc_add function to add numbers, gives correct answer
      total = mf.calc_add(num1, num2)
      
      # determine if user answered equation correctly 
      # user gets 2 guesses until they are shown correct answer
      # initialize to 0, 2 respectively
      attempts = 0
      max_attempts = 2
      
      while attempts < max_attempts:
        # user's answer to equation
        user_answer = int(input(f"{num1} + {num2} = "))
        
        # compare user's answer to correct answer
        if user_answer == total:
            print("Correct! Well done! :)\n")
            
            # Set attempts to max attempts to exit the loop
            attempts = max_attempts
        else:
            
          print("EEE!!! Incorrect answer.\n")
        
          # keep track of user's attempts
          attempts += 1
      
      # show correct answer to equation  
      if attempts == max_attempts:
          print("The correct answer is...")
          print(f"{num1} + {num2} = {total}\n") 

      # Chat GPT: suggested assigning user_choice as variable to the repeat
      # option function
      # Prompt: how can i get the main menu to come back up in or after the 
      # Menu for user to choose between repeating function or 
      # returning to main menu
      user_choice = repeat_option()

    print("Returning to the main menu...\n")
  except ValueError:
    print("Invalid input! Please enter a valid integer.\n")

def subtract():
  """
  Function subtracts 2 numbers that the user inputs
  Calls function to do the math and another to repeat the function
  """

  try:
    user_choice = 1  # Initialize to 1 to enter the loop

    while user_choice == 1:
      print("Subtract")
      
      # call get_numbers() function
      num1, num2 = get_numbers()

      total = mf.calc_subtract(num1, num2)
      
      # determine if user answered equation correctly 
      # user gets 2 guesses until they are shown correct answer
      # initialize to 0, 2 respectively
      attempts = 0
      max_attempts = 2
      
      while attempts < max_attempts:
        # user's answer to equation
        user_answer = int(input(f"{num1} - {num2} = "))
        
        # compare user's answer to correct answer
        if user_answer == total:
            print("Correct! Well done! :)\n")
            
            # Set attempts to max attempts to exit the loop
            attempts = max_attempts
        else:
            
          print("EEE!!! Incorrect answer.\n")
        
          # keep track of user's attempts
          attempts += 1
      
      # show correct answer to equation  
      if attempts == max_attempts:
          print("The correct answer is...")
          print(f"{num1} - {num2} = {total}\n")
      
      user_choice = repeat_option()
      
    print("Returning to the main menu...\n")
    
  except ValueError:
    print("Invalid input! Please enter a valid integer.\n")

def divide():
  """
  Function divides 2 numbers that the user inputs
  Calls function to do the math and another to repeat the function
  """
  try:
    user_choice = 1  # Initialize to 1 to enter the loop

    while user_choice == 1:
      print("Divide")
      
      # call get_numbers() function
      num1, num2 = get_numbers()
  
      quotient = mf.calc_divide(num1, num2)
      
      # determine if user answered equation correctly 
      # user gets 2 guesses until they are shown correct answer
      # initialize to 0, 2 respectively
      attempts = 0
      max_attempts = 2
      
      while attempts < max_attempts:
        # user's answer to equation
        user_answer = int(input(f"{num1} / {num2} = "))
        
        # compare user's answer to correct answer
        if user_answer == quotient:
            print("Correct! Well done! :)\n")
            
            # Set attempts to max attempts to exit the loop
            attempts = max_attempts
        else:
            
          print("EEE!!! Incorrect answer.\n")
        
          # keep track of user's attempts
          attempts += 1
      
      # show correct answer to equation  
      if attempts == max_attempts:
          print("The correct answer is...")
          print(f"{num1} / {num2} = {quotient}")

      user_choice = repeat_option()
      
    print("Returning to the main menu...\n")
      
  except ZeroDivisionError:
    
    print("Cannot divide by 0!\n")
  

def multiply():
  """
  Function multiplies 2 numbers that the user inputs
  Calls function to do the math and another to repeat the function
  """
  try:
    user_choice = 1  # Initialize to 1 to enter the loop

    while user_choice == 1:
      print("Multiply")
      # call get_numbers() function
      num1, num2 = get_numbers()
      
      product = mf.calc_multiply(num1, num2)
      
      # determine if user answered equation correctly 
      # user gets 2 guesses until they are shown correct answer
      # initialize to 0, 2 respectively
      attempts = 0
      max_attempts = 2
      
      while attempts < max_attempts:
        # user's answer to equation
        user_answer = int(input(f"{num1} * {num2} = "))
        
        # compare user's answer to correct answer
        if user_answer == product:
            print("Correct! Well done! :)\n")
            
            # Set attempts to max attempts to exit the loop
            attempts = max_attempts
            
        else:
            
          print("EEE!!! Incorrect answer.\n")
        
          # keep track of user's attempts
          attempts += 1
      
      # show correct answer to equation  
      if attempts == max_attempts:
          print("The correct answer is...")
          print(f"{num1} * {num2} = {product}")
      
      user_choice = repeat_option()
      
    print("Returning to the main menu...\n")
    
  except ValueError:
    
    print("Invalid input! Please enter a valid integer.\n")
  
def repeat_option():
  """
  Function presents menu to either repeat function or return to main
  menu, takes user input, and returns their choice
  """
  print("1. Repeat")
  print("2. Main Menu")
  
  user_choice = int(input("Enter a number: "))
  
  return user_choice