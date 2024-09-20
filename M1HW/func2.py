def add():
  try:
    user_choice = 1  # Initialize to 1 to enter the loop

    while user_choice == 1:
        print("Add")
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        sum = num1 + num2
        
        print_add(num1, num2, sum)
        print("1. Repeat")
        print("2. Main Menu")
        user_choice = int(input("Enter a number: "))
    
    print("Returning to the main menu...")
  except ValueError:
    print("Invalid input! Please enter a valid integer.\n")

# Example of calling the add() function
# add()

# function to print out correct answer to ADD equation
def print_add(num1, num2, sum):
  print(f"{num1} + {num2} = {sum}")
  
# function to print out correct answer to SUBTRACT equation
def print_subtract(num1, num2, sum):
  print(f"{num1} - {num2} = {sum}")

# function to print out correct answer to DIVIDE equation
def print_divide(num1, num2, remainder):
  print(f"{num1} / {num2} = {remainder}")

# function to print out correct answer to MULTIPLY equation
def print_multiply(num1, num2, sum):
  print(f"{num1} * {num2} = {sum}")