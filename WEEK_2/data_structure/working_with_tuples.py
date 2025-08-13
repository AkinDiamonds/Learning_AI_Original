# creating tuples
# using parenthesis ()
# Example 1: tuple with multiple items
fruits = ('apple', 'banana', 'cherry')
print(fruits) # ('apple', 'banana', 'cherry')

# without parenthesis (tuple packing)
numbers = 1, 2, 3
print(numbers) # (1,2,3)

# single-item tuple (must include a comma)
single_item = ("apple,")
print(single_item) # ('apple',)
print(type(single_item)) # <class 'tuple'>

# using the tuple() constructor
fruits_list = ["apple", "banana", "cherry"]
fruits_tuple = tuple(fruits_list)
print(fruits_tuple) # ('apple', 'banana', 'cherry')

# characteristics of tuples
# ordered
colors = ("red", "green", "blue")
print(colors[0]) # red
# immutable (uncomment and run. This will cause an error)
#colors[1] = "yellow" # typeerror

# allow duplicates
numbers2 = (1, 2, 2, 3)
print(numbers2) # (1, 2, 2, 3)
# mixed data types
mixed = ("apple", 3, True, 5.6)
print(mixed)    # ('apple', 3, True, 5.6)
# nested tuples
nested = (("a", "b"), (1, 2))
print(nested)   # (('a', 'b'), (1, 2))

# tuple operations
# indexing
fruits2 = ("apple", "banana", "cherry")
print(fruits2[1]) # banana
print(fruits2[-1]) # cherry
# slicing
print(fruits2[0:2]) # ('apple', 'banana')
print(fruits2[::-1]) # ('cherry', 'banana', 'apple')
# concatenation
tuple1 = (1, 2)
tuple2 = (3, 4)
result = tuple1 + tuple2
print(result)
# repetition
nums = (1, 2)
print(nums *3)  # (1, 2, 1, 2, 1, 2)
# membership
fruits3 = ("apple", "banana", "cherry")
print("banana" in fruits3) # True
print("grape" not in fruits3) # True
# iteration
for fruit in fruits3:
    print(fruit)

# you cant modify a tuple directly, but you can convert it to a list, modify it and convert it back to a tuple.
# unpacking tuples
person = ("John", 25, "Nigeria") 
name, age, country = person
print(name) # John
print(age) # 25
print(country) # Nigeria

# tuple methods
# tuples have only two methods
# dot count() and dot index()
numbers3 = (1, 2, 2, 3, 4)
print(numbers3.count(2)) # 2 (counts occurrence of 2)
print(numbers3.index(3)) # 3 (position of first occurence of 3)

# converting between list and tuple
# tuple to  list
t = (1, 2, 3)
lst = list(t)
lst.append(4)
print(lst) # [1, 2, 3, 4]

# list back to tuple
t = tuple(lst)
print(t) # (1, 2, 3, 4)

# built-in functions with tuples
nums1 = (4, 1, 7, 3)
print(len(nums1)) # 4
print(max(nums1)) # 7
print(min(nums1)) # 1
print(sum(nums1)) # 15