# Write a program that collects the names of people 
# attending a seminar (no duplicates allowed) and displays
#  them in alphabetical order.

# assign input to variable: name
# change "name" to set: unique_name
# sort unique_name and assign to: sorted_name
# print sorted_name

name = input("Enter your name: ")
unique_name = {name, "Bayo", "Toba", "Jimoh"}
sorted_name = sorted(unique_name)
print(sorted_name)