# **Task2: Tuple and Input**

# - Ask the user for 5 best friends’ names.

# - Store them in a tuple friends.

# - Print the tuple in reverse order.

lst_friends = input("Enter the names of your 5 best friends (seperated with spaces): ").split()
friends = tuple(lst_friends)
print(friends[::-1])