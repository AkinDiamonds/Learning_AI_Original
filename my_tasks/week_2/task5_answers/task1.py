# **Task1:  Create and Display**

# - Ask the user to enter three favorite Nigerian dishes (one at a time).

#  - Store them in a tuple called dishes.

# - Print the tuple in a single line, separating items with commas.

# - Use the \n escape sequence to print each dish on a new line.

while True:             # my while loop. was not there before
      try:
            dish1 = input("Enter your favourite Nigerian dish: ")
            if not dish1.split():            # this error handling code is for customers who input only empty spaces
                  raise ValueError("You didn't type anything. Kindly enter your favourite Nigerian dish.")
            dish2 = input("Enter another favourite Nigerian dish: ")
            if not dish2.split():
                  raise ValueError("You didn't type anything. Kindly enter another favourite Nigerian dish.")
            dish3 = input("Enter another favourite Nigerian dish: ")
            if not dish2.split():
                  raise ValueError("You didn't type anything. Kindly enter your 3rd favourite Nigerian dish.")
            all_dish = [dish1, dish2, dish3]
            dishes = tuple(all_dish)
            print(", ".join(dishes), "\n")
            for dish in dishes:                       # this is my for loop
                  print(f"{dish}\n")
      except ValueError:
            print("Value Error")          # just something they can understand.