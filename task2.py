# **Task2: Super Market Price List**
# - Create a program that stores items and their prices in a dictionary.

#   - Items should come from a list.

#   - Prices are entered by the user.

#   - Display all items and prices, then allow the user to update the price of an item.

# - Requirements:

#   - Use dictionary update method `.update()` or assignment.

#   - Use `.keys()` to display available items.

#   - Use input validation (no advanced functions).

book = float(input("Enter the price of book: "))
pencil = float(input("Enter the price of pencil: "))
crayon = float(input("Enter the price of crayon: "))
pen = float(input("Enter the price of pen: "))
items = ["book", "pencil", "crayon", "pen"]
store = {items[0]: book, items[1]: pencil, items[2]: crayon, items[3]: pen}
print(f'Supermarket Price List\n',
      'Items\t', 'Prices\n',
      f'{items[0]}\t', f'{store[items[0]]}\n',
      f'{items[1]}\t', f'{store[items[1]]}\n',
      f'{items[2]}\t', f'{store[items[2]]}\n',
      f'{items[3]}\t', f'{store[items[3]]}\n')

# allow user to update dictionary
update1 = float(input(f"Enter the price of {items[0]}: "))
update2 = float(input(f"Enter the price of {items[1]}: "))
update3 = float(input(f"Enter the price of {items[2]}: "))
update4 = float(input(f"Enter the price of {items[3]}: "))
store[items[0]] = update1
store[items[1]] = update2
store[items[2]] = update3
store[items[3]] = update4
print(f'Updated Supermarket Price List\n',
      'Items\t', 'Prices\n',
      f'{items[0]}\t', f'{store[items[0]]}\n',
      f'{items[1]}\t', f'{store[items[1]]}\n',
      f'{items[2]}\t', f'{store[items[2]]}\n',
      f'{items[3]}\t', f'{store[items[3]]}\n')