# **Task2: Super Market Price List**
# - Create a program that stores items and their prices in a dictionary.

#   - Items should come from a list.

#   - Prices are entered by the user.

#   - Display all items and prices, then allow the user to update the price of an item.

# - Requirements:

#   - Use dictionary update method `.update()` or assignment.

#   - Use `.keys()` to display available items.

#   - Use input validation (no advanced functions).
items = ["sugar", "salt", "kilishi", "macbook", "scotch egg"]
sugar = input(f"Enter price of {items[0]}")
salt = input(f"Enter price of {items[1]}")
kilishi = input(f"Enter price of {items[2]}")
macbook = input(f"Enter price of {items[3]}")
scotch_egg = input(f"Enter price of {items[4]}")
dictionary = {items[0]: sugar, items[1]: salt, items[2]: kilishi, items[3]: macbook, items[4]: scotch_egg}
print(dictionary)
update_price = input("Do you want to update the price of an item? ").lower()
if update_price == 'yes':
    print(f"Available items: {dictionary.keys()}")