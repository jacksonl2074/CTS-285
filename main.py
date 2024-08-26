"""
CTS 285
M1HW - Calculator
Laura K. Jackson
9/2/2024
"""
# import functions module
import functions as fn
import func2 as f2

# constants
ADD = 1
SUBTRACT = 2
DIVIDE = 3
MULTIPLY = 4
EXIT = 5

def main():
  choice = 0

  while choice != EXIT:

    # call display menu function
    menu()

    choice = int(input("Enter your choice: "))

    # decision structure based on user input
    if choice == ADD:
      # call Add function
      f2.add()
    elif choice == SUBTRACT:
      fn.subtract()
    elif choice == DIVIDE:
      fn.divide()
    elif choice == MULTIPLY:
      fn.multiply()
    elif choice == EXIT:
      print("Exiting program...Goodbye! :)")
    else:
      print("Invalid input. Please try again.\n")
      
# menu function
def menu():
  
    print("Welcome to the Calculator Program!")
    print("1. Add")
    print("2. Subtract")
    print("3. Divide")
    print("4. Multiply")
    print("5. Exit")
    

if __name__ == "__main__":
  main()