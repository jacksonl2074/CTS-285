"""
CTS 285
M1HW - Calculator
Laura K. Jackson
9/2/2024
"""
# import functions module
import functions as fn


# constants
ADD = 1
SUBTRACT = 2
DIVIDE = 3
MULTIPLY = 4
EXIT = 5

def answer_checker():
  """
  Function calls menu function, allows user to pick an option for doing
  math equations
  """
  choice = 0

  while choice != EXIT:
    
    try:
      # call display menu function
      menu()
  
      choice = int(input("Enter your choice: "))
  
      # decision structure based on user input
      if choice == ADD:
        # call Add function
        fn.add()
      elif choice == SUBTRACT:
        fn.subtract()
      elif choice == DIVIDE:
        fn.divide()
      elif choice == MULTIPLY:
        fn.multiply()
      elif choice == EXIT:
        print("\nExiting Answer Checker...Goodbye! :)\n")
      else:
        print("Invalid input. Please try again.\n")
  
    except ValueError:
      print("Invalid input! Please enter a number.\n")
        
      
# menu function
def menu():
  """
  Function displays menu to user
  """
  print("Welcome to the Calculator Program!")
  print("1. Add")
  print("2. Subtract")
  print("3. Divide")
  print("4. Multiply")
  print("5. Exit")
    
# call main()
# if __name__ == "__main__":
  # main()