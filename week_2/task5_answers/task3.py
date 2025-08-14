# **Task3: Tuple Operations**
# - Create a tuple of 5 Nigerian states entered by the user.

#   - Print the first state and last state.

#   - Check if "Lagos" is in the tuple and print "Yes" or "No".

#   - Print the number of states entered.
#     - (Hint: use the tuple membership)

states = input("Enter 5 Nigerian states(seperated by commas): ").split()
tuple_states = tuple(states)
print(tuple_states[0], tuple_states[-1])
check_word = "Lagos"
print("Yes" if check_word in tuple_states else "No")
