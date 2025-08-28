# A module is a file with .py extension that contains Python code (functions, variables, or classes) which can be reused in other programs.

# Different ways to import modules
# 1. Import the whole module
import math
# Let's put it to use
print(math.sqrt(9))
# Note that you must specify the module name when calling a function within it.

# 2. import as an alias
import math as m
# lets put it to use
print(m.sqrt(25))
# - This shortens the module name, this is common with libraries like numpy, pandas, etc.

# 3. Import specific functions or variables
from math import sqrt, pi, sin
print(sqrt(36))
print(pi)
print(sin(90))
#  - here you dont need the prefix 'math' anymore

# 4. Import everything from the module
from math import *
print(sqrt(49))
print(pi)
# This is usually not recoommended because it can cause name conflicts if two modules have functions with the same name.

# Writing your own module
# step1: Create a folder. Name it my_module
# Step2: Create a file inside the folder. Name it first.py
# step3: Create another file inside the same folder. Name it second.py
# step4: Create another file still inside same folder. Name it main.py

# my_module/first.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"
    
#  my_module/second.py
def greet(name):
    return f"Hello, {name}! I am creating my own module"

def reverse_string(string):
    return string[::-1]

def count_characters(string):
    return len(string)

def count_words(string):
    return len(string.split())

# my_module/main.py
import first
import second
# lets use the functions in the first.py file

print("=== Math functions ===")
print("5 + 3 =", first.add(5,3))
print("10 - 4 =", first.subtract(10, 4))
print("6 * 7 =", first.multiply(6, 7))
print("20 / 5 =", first.divide(20, 5))

# Let's use the functions in the second.py file
print("\n=== String Functions ===")
print(second.greet("Ridwan"))
print("Reverse of 'Python' =", second.reverse_string("Python"))
print("Character count in sentence =", second.count_characters("Python modules are powerful"))
print("Word count in sentence =", second.count_words("Python modules are powerful"))



# A package is a way to organize related modules together into a folder.
# inside this folder, there must be a special file called __init__.py (can be empty). This file tells Python that the folder should be treated as a package.


# how to install python packages
# using pip (you have to use in your terminal)

# pip install requests  (Install latest version)
# pip install requests==2.28    (Install specific version)
# pip install --upgrade requests    (Upgrade existing package)
# pip uninstall requests    (Remove package)

# using uv
# This is the modern, super-fast package and project manager
# to use uv
# run this command on your terminal depending on your OS
# recommended method: standalone installer
# macOS/Linux
# curl - LsSf https://astral.sh/uv/install.sh | sh

# or

# Windows
# powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
# after installation, verify version
# uv --version

# but before it works you must have a working virtual environment
# uv add requests   # Install package and update project files
# uv pip install flask  # Works like pip but much faster
# uv venv       # Create a virtual environment automatically
# uv run script.py  # Run scripts in the managed environment


# Creating your package
# ```
# my_project/
# │
# ├── my_package/              # Package folder
# │   ├── __init__.py          # Makes this folder a package
# │   ├── math_utils.py        # Module 1
# │   ├── string_utils.py      # Module 2
# │
# └── main.py                  # Script that uses the package

# ```
# __init__.py is a special file you create in your package folder (can be empty) that tells Python that the folder is a package.

# __init__.py
print("my_package is being imported")
# Optional: import functions directly for easier access
from .math_utils import add, subtract
from .string_utils import capitalize_text

# module for maths operations
# math_utils.py
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b

# module for string operations
# string_utils.py
def capitalize_text(text):
    return text.capitalize()

def reverse_text(text):
    return text[::-1]