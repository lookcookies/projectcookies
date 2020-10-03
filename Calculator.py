# --- Calculator Structure ---
# Options list
# Select option
# Input first number
# Input second number

def list():
    print("Functions list: \n1. Addition \n2. Subtraction")

# Addition
def addition():
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print(x + y)
    return


# Subtraction
def subtraction():
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print(x - y)
    return


# Function options
def options():
    pick_function = int(input("Pick a function:"))
    if pick_function == 1:
        pick_function = addition()
    elif pick_function == 2:
        pick_function = subtraction()

    if (pick_function != 1 or 2):
        print(int(input("Invalid function. Pick a function: ")))
    else:
        options()
# User inputs numbers
def calculator(option=None):
    list()
    options()
    return

# Run calculator
calculator()
