# Errors in Python are classified into three main categories:
# Syntax Errors, Runtime Errors and Semantic Errors

# SYNTAX ERRORS
# it occurs when the Python interpretern cannot understand your code because it breaks Python grammar rules.
# IndentationError - Incorrect Spacing
for i in range(3):
print(i) # wrong indentation
# This will through error except you fix the indentation.
Cell In[2], line 2
print(i) # wrong indentation
IndentationError: expected an indented block after 'for' statement on line 1

# Missing colon/parenthesis error
if 5 > 3    # missing colon
    print("Hello")

# Invalid Syntax - General grammar mistakes.
print "Hello" # Missing parentheses in Python 3

# To fix: Double check Python grammar, colons, parentheses, and indentation.

# RUNTIME ERRORS
# The program is syntactically correct, but an error occurs while it is running.
# These are also called  exceptions.
# They can be handled with try, except, and finally.

# Common subtypes of runtime errors

# ZeroDivisionError - Dividing by zero.
x = 10 / 0 # This will throw error

# NameError - Using a variable before defining it.
print(age) # age not defined

# TypeError - Wrong data type in an operation.
result = "10" + 5 # str + int not allowed

# ValueError - Invalid value for a function.
number = int("abc") # cannot convert string to int

# IndexError - Accessing list index out of range.
fruits = ["apple", "banana"]
print(fruits[3]) # Index out of range

# KeyError - Accessing a dictionary with a missing key.
data = {"name": "Ada"}
print(data["age"]) # Key not found

# FileNotFoundError - File does not exist
f = open("missing.txt") # File not found

# Handling Runtime Errors
# Python provides exception handling to prevent programs from crashing when unexpected errors occur.
# The keywords are:
# try - block of code to test for errors.
# except - block of code that runs if an error occurs.
# finally - block of code that always runs (whether error occurs or not).

# The try Block
# it is used to wrap code that might raise an error.
# if no error occurs, Python skips the except block.
try:
    x = 10 / 2
    print("Result: ", x)

# The except block
# it defines what to do if an error occurs inside try.
# it can catch specific errors or all errors.

# this is a specific exception
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide zero")

# this is a case of multiple exception
try:
    number = int("abc")     # ValueError
    result = 10 / 0         # ZeroDivisionError
except ValueError:
    print("Invalid conversion to integer.")
except ZeroDivisionError:
    print("Cannot divide by zero.")

# The finally Block
# Always runs, whether an error occurred or not.
# Useful for cleanup tasks (e.g. closing files, releasing resources).

try:
    f = open("sample.txt", "r")
    content = f.read()
except FileNotFoundError:
    print("File not found.")
finally:
    print("Closing file if it was opened.")

# more examples
balance = 5000  #   starting balance
print("Welcome to the ATM")
amount = input("Enter amount to withdraw: ")

try: 
    amount = float(amount) # convert input to number
    if amount > balance:
        raise ValueError("Insufficient funds.")
    
    balance -= amount
    print("Withdrawal successful. New balance: ₦", balance)

except ValueError as e:
    print("Error:", e)

except Exception as e:
    print("Unexpected error:", e)

finally:
    print("Transaction session closed.")

# If user enters 2000
# - Withdrawal successful. New balance: ₦ 3000.0
# - Transaction session closed.

# if user enters 6000
# - Error: Insufficient funds.
# - Transaction session closed.

# if user enters abc
# - Error: could not convert string to float: 'abc'
# - Transaction session closed.

# SEMANTIC ERRORS
# the code runs without crashing, but the output is logically wrong.
# hardest to detect because the interpreter sees no error.
# Semantic errors are mostly logic mistakes, so subtypes are based on how the logic is wrong.
# Note that semantic errors are not officially exceptions in Python, but they are real mistakes programmers make when the logic is wrong.

# Common Subtypes of Semantic Errors

# Wrong Condition in Logic
age = 18
if age > 18:    # Should be >=
    print("Eligible to vote")
else:
    print("Not eligible")
#  Not eligible (wrong result)

# Wrong Formula/Computation
length = 10
width = 5
area = length + width   # should be multiplication
print("Area:", area)
# 15 (expected 50)

# Wrong Variable Usage
marks = [70, 80, 90]
total = marks[0] * marks[1] * marks[2] # wrong. should be sum
print("Total:", total)

# To fix semantic errors, carefully review logic, test with multiple cases, use debugging or print statements.