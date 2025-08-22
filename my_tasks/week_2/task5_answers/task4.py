# **Task4: Tuple Unpacking**
#  - Ask a user for their;

#   - First name

#   - Age

#   - Favorite color

#   - Home town

#   - Store them in a tuple profile and unpack into variables.

#   - Print and use  escape sequence to align each piece of information nicely.

# assign all variables to input
# arrange into a tuple
# unpack variables
# print
shell = True
while shell:
      try:
            first_name = input("Enter your first name: ")
            if any(char.isdigit for char in first_name):
                  raise ValueError("You're not a Macbook, right? Enter your real name.")
            else:
                  age = input("Enter your age: ")
            if age.isdigit != True:
                  raise ValueError
            else:
                  print("Please enter numbers instead.")
            color = input("Enter your favorite color: ")
            town = input("Enter your home town: ")
            profile = (first_name, age, color, town)
            name, your_age, your_color, home_town = profile
            print("Your name: \t", f'{name}\n'
      "Your age: \t", f'{your_age}\n'
      "Your color: \t", f'{your_color}\n'
      "Your hometown: \t", f'{home_town}\n')
      except Exception:
            print("Value Error")
