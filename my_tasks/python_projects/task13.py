"""
Overview An Email Slicer is a simple yet useful tool that
extracts the username and domain from an email address.
This project enhances understanding of string manipulation,
user input handling, and string slicing in Python.
This project covers the step-by-step implementation of an
Email Slicer, including handling user input, extracting the
username and domain, and displaying the results.

Key Concepts of Email Slicer in Python

String Manipulation:

- Using string methods like split() and
- Extracting specific parts of a string

User Input Handling:

- Accepting an email address from the user
- Validating the input format

Output Formatting:

- Displaying extracted username and domain clearly
"""

# function to slice the input
# call and validate function
# display if validated
# else, ask to input again
try:
    def slicer(email) -> tuple:
        if email.count("@") == 1 and email.count(".") == 1:
            username, domain = email.split("@")
            return username, domain
        else:
            print("You entered an invalid email address!")
        return (None, None)


    email = input("Enter a valid email address: ")
    
    username, domain = slicer(email)
    if username and domain:
        print(f"Username: {username}\n \
        Domain: {domain}")
except Exception as e:
    print("Error:", e)