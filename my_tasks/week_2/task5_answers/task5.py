# **Task5: Modify Tuple Indirectly**
# Ask a user to enter three items for their shopping list.

#   - Store in a tuple shopping_list.

#   - Convert it to a list, then ask for two more items to add.

#   - Convert back to a tuple and print the updated list using join() to display items separated by " | ".

# assign variable user to user's input
# typecast into tuple and assign variable shopping_list
# assign variable: new_input to a new input with dot split
# add user to new_input and assign to variable: shopping_list2
# print shopping_list2 using join(|)

user = input("Enter 3 items for your shopping list(separated by spaces): ").split()
shopping_list = tuple(user)
new_input = input("Enter 2 more items to add: ").split()
shopping_list2 = new_input + user
shopping_list3 = tuple(shopping_list2)
print("|".join(shopping_list2))