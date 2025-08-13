# creating sets
# using curly brackets
fruits = {"apple", "banana", "mango"}
print(fruits)

# using the set() constructor
numbers = set ([1, 2, 3, 4])
print(numbers)

# creating an empty set (must use set(), not {})
empty_set = set()
print(empty_set)

# from a string (duplicates removed automatically)
letters = set("mississippi")
print(letters)

#set operations
# adding elements
colors= {"red", "blue"}
colors.add("green")
print(colors)
# removing elements
colors.remove("blue") # Removes an element, raises error if not found
colors.discard("yellow") # Removes if found, no error if missing
print(colors)
# pop an element
colors1 = {"red", "blue", "green"}
removed = colors.pop()
print("Removed: ", removed)
print("Remaining: ", colors1)

#clear set
colors.clear()
print(colors)

# mathematical set operations
set1 = {1,2,3,4}
set2 = {3,4,5,6}

# union
print(set1 | set2)
print(set1.union(set2))

# intersection
print(set1 & set2)
print(set1.intersection(set2))

# difference
print(set1 -set2)
print(set1.difference(set2))

# symmetric difference
print(set1 ^ set2)
print(set1.symmetric_difference(set2))

# working with sets
# collecting unique visitors to an event
visitors = set()

# adding visitors
visitors.add("Chinedu")
visitors.add("Aisha")
visitors.add("Chinedu") # duplicate, ignored automatically
print("Visitors: ", visitors)

# checking if a visitor attended
name = "Aisha"
if name in visitors:
    print(f"{name} attended the event.")
else:
    print(f"{name} did not attend the event.")
