# **Task1:  Create and Display**

# - Ask the user to enter three favorite Nigerian dishes (one at a time).

#  - Store them in a tuple called dishes.

# - Print the tuple in a single line, separating items with commas.

# - Use the \n escape sequence to print each dish on a new line.

dish1 = input("Enter your favourite Nigerian dish: ")
dish2 = input("Enter another favourite Nigerian dish: ")
dish3 = input("Enter another favourite Nigerian dish: ")
all_dish = [dish1, dish2, dish3]
dishes = tuple(all_dish)
print(dishes)
print(f"{dishes[0]}\n"
      f"{dishes[1]}\n"
      f"{dishes[2]}\n")