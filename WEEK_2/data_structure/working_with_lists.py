# How to create a list
# Method 1: Using square brackets
empty_list = []
print(empty_list) # Output:[]

# Method 2: Using the list() constructor
empty_list2 = list()
print(empty_list2) # Output: []

# Creating a list with initial elements
# List of integers
numbers = [1, 2, 3, 4, 5]
print(numbers) # Output: [1, 2, 3, 4, 5]

# List of strings
fruits = ["apple", "banana", "cherry"]
print(fruits) # Output: ['apple', 'banana', 'cherry']

# Mixed data types
mixed_lists = ["Alice", 25, 5.8, True]
print(mixed_lists) # Output: ['Alice', 25, 5.8, True]

# From a string (each character becomes an element)
chars = list("hello")
print(chars) # Output: ['h', 'e', 'l', 'l', 'o',]

# From a tuple
my_tuple = (10, 20, 30)
list_from_tuple= list(my_tuple)
print(list_from_tuple) # Output: [10, 20, 30]

# From a range
numbers_range = list(range(5)) 
print(numbers_range) # Output: [0,1,2,3,4]

# Squares of numbers 0-4
squares = [x**2 for x in range(5)]
print(squares) # Output: [0, 1, 4, 9, 16]

# Even numbers between 0-10
evens = [x for x in range(11) if x % 2 ==0]
print(evens) # Output: [0, 2, 4, 6, 8, 10]

# Creating a Nested list. List in a list.
# Matrix-like list
matrix = [[1,2], [3, 4], [5, 6]]
print(matrix) # Output: [[1, 2], [3, 4], [5, 6]]

# Accessing elements in a nested list
print(matrix[0]) # Output: [1, 2]
print(matrix[0][1]) # Output: 2

# Characteristics
# Ordered
fruits2 = ['mango', 'orange', 'banana']
print(fruits2) # ['mango', 'orange', 'banana']
print(fruits2[0]) # mango
print(fruits2[2]) # banana

# Allows Duplicates
items = ["rice", 'beans', "yam", 'rice']
print(items) # ['rice', 'beans', 'yam', 'rice']

# Mutable
numbers2 = [1, 2, 3]
numbers2[1] = 'fine' # Changing element at index 1
print(numbers2) # [1, 'fine', 3]

# Mixed data types
mixed = [10, "Nigeria", 3.14, True]
print(mixed)  # [10, 'Nigeria', 3.14, True]

# Can be nested
nested_list = [[1, 2], ["a", "b"]]
print(nested_list)       # [[1, 2], ['a', 'b']]
print(nested_list[0][1]) # 2

# Dynamic size
names = ['Ada']
names.append('Bola')
names.append('Chidi')
print(names)