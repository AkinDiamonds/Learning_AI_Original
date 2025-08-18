# create dictionary: "store"
store = {"Book":500000, "Pen": 10000, "Bag": 50000}
print(f"Before purchase: {store}")

# user's input
item = input("Input an item you want to buy: ").title()
quantity = int(input("Input the quantity you want to purchase: "))

# update dictionary
store[item] -= quantity

# display
print(f"After purchase: {store}")