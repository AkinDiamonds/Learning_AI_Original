# **Task4: Unique Members Registration**
# - Ask the user to enter three names separated by commas.

#    - Convert them to a set to ensure uniqueness.

#    - Create a dictionary where each name is a key and its length is the value.

# - Requirements:

#    - Use `.split(",")` and `set()` to remove duplicates.

#    - Use dictionary comprehension `{name: len(name) for name in set_of_names}`.

# collect data
names = set(input("Enter 3 names separated by a comma: ").split())
print(names) 
# set up length of names in a dictionary
name_length = {name: len(name) for name in names}
print(name_length)