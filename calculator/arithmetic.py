""""
create functions that is capable of adding, subtracting, multiplying and dividing two numbers together.
then, return the answers back to the function.
"""

# Addition
def add(a, b):
    return a + b

# Subtraction
def subtract(a, b):
    return a - b

# Multiplication
def multiply(a, b):
    return a * b

# Division
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero."
    return a / b