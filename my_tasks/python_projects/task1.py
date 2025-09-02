"""
A basic calculator is one of the fundamental
projects in Python programming. It provides essential
arithmetic operations such as addition, subtraction,
multiplication, and division. Understanding how to
implement a calculator helps in learning user input
handling, conditional statements, and function creation in
Python.

Key Concepts of Basic Calculator in Python
 Arithmetic Operations:
 Addition ( + )
 Subtraction (- )
 Multiplication ( * )
 Division ( / )
 Modulus ( % )
 Exponentiation ( ** )
 User Input Handling:
 Using input() function
 Converting strings to integers or floats
 Functions in Python:
 Defining functions for calculations
 Calling functions with user inputs
 Error Handling:
 Parameter Table
 Operator
 Handling division by zero
 Handling invalid inputs
 """

# addition function
# subtraction function
# multiplication function
# Division function
# modulus function
# exponentiation function
# input operation
# use condition for operations
# handle errors

# define functions
"""
a function that collects multiple inputs from user and returns the sum
"""
def add(arg):
    result = 0
    for number in arg:
        result += int(number)


values = input("Enter the numbers you want to add(separated by space): ")

add(values.split())

# def subtract(*values):
#     values = input("Enter the numbers you want to subtract").split()
#     for i in values:
        

# def multiply(*values):
#     return 

