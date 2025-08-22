# write a program to take a string from the user and display it in uppercase.
# Given the string "python", print its first and last characters.
#  Ask the user for their name and print "Hello, [user's input]"
# Write a program to count the number of characters in string without using len().
# given "Hello World", replace "World" with "Python".

# 1.
string = input("Enter anything in lowercase: ").upper()
print(string)

# 2.
string = "python"
print(string[0], string[5])

# 3.
name = input("Enter your name: ")
print("Hello, ", name, ".")

# 4.
name = "Simeon"
length = name.find(name[-1]) + 1
print(length)

# 5. 
name = "Hello World"
print(name.replace("World", "Python"))