# functions for each choice in calculator

def add():
  print("Add")
  num1 = int(input("Enter first number: "))
  num2 = int(input("Enter second number: "))
  # FIXME: create diff function to add numbers and display
  sum = num1 + num2
  print(f"{num1} + {num2} = {sum}")
  
  user_choice = 0
  
  while user_choice != 2:
    print("1. Repeat")
    print("2. Main Menu")
    user_choice = int(input("Enter a number: "))

def subtract():
  print("Subtract")
  num1 = int(input("Enter first number: "))
  num2 = int(input("Enter second number: "))
  sum = num1 - num2
  

def divide():
  print("Divide")
  num1 = int(input("Enter first number: "))
  num2 = int(input("Enter second number: "))
  
  try:
    remainder = num1 / num2
    # print(f"{num1} / {num2} = {remainder}")
  except ZeroDivisionError:
    print("Cannot divide by 0!\n")
  # FIXME: need to present choices to repeat or return to main menu
          

def multiply():
  print("Multiply")
  num1 = int(input("Enter first number: "))
  num2 = int(input("Enter second number: "))
  
  sum = num1 * num2
  
  