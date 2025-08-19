# python dictionary: aa collection of key-value pairs
#syntax
#dictionary_name = {key1: value1, key2: value2}

# creating dictonaries

# usinig curly braces
student = {
    "name": "Ada",
    "age": 20,
    "course": "Computer Science"
}
print(student)

# using the dict() constructor
student_info = dict (name="John", age=25, course = "Maths")
print(student_info)

# empty dictionary
empty_dict = {}
print(empty_dict)

# dictinary comprehension
# syntax
# {key_expression: value_expression for item in item in iterable if condition}

# create a dictionary of numbers and their squares
squares = {x: x**2 for x in range(1, 6)}
print(squares)

# with condition
# dictionary of even numbers and their cubes
evens_cube = {x: x**3 for x in range(1, 10) if x % 2 == 0}
print(evens_cube)

# from existing dictionary
students = {"Ada": 85, "John": 40, "Musa": 65}
# filter students who passed (score > = 50)
passed_students = {name: score for name, score in students.items() if score >= 50}
print(passed_students)

# using strings keys
names = ["Ada", "John", "Musa"]
lengths = {name: len(name) for name in names}
print(lengths)

# accessing dictionary items
# define a dictionary
student1 = {"name": "Ada", "age": 20, "course": "Computer Science"}

# using key
print(student1["name"])

# using get() method (avoids error if key is missing)
print(student1.get("age"))
print(student1.get("grade", "Not Found"))

# modifying dictionaries
student1["age"] = 21 # Change value 
student1 ["grade"] = "A" # Add new key-value pair print(student)

# Removing items from dictionaries

# using pop()
student1.pop("grade")

# using popitem() - removes last inserted key-value
student1.popitem()
# using del keyword
# del student1["course"]
# using clear() - removes all items
student1.clear()

print(student1)

# dictionary methods
person = {"name": "Emeka", "age": 30}

# keys()
print(person.keys())
# values()
print(person.values())
# items()
print(person.items())
# update()
person.update({"age": 31, "city": "Lagos"})
print(person)

# nested dictionaries
stuudents = {
    "student1": {"name": "Ada", "age": 20},
    "student2": {"name": "John", "age": 22}
}
print(stuudents["student1"]["name"])

# looping through dictonaries
# define a dictionary
studentt = {"name": "Ada", "age": 20, "course": "Computer Science"}
# loop through keys
for key in studentt:
    print(key)
# loop through values
for value in studentt.values():
    print(value)
# loop through key-values pairs
for key, value in studentt.items():
    print(f"{key}: {value}")

# storing a student's biodata
student4 = {
    "name": "Chinedu",
    "age": 19,
    "department": "Engineering",
    "subjects": ["Maths", "Physics", "Chemistry"],
    "is_full_time": True
}

print(f"Name: {student4["name"]}")
print(f"Subjects: {', '.join(student4["subjects"])}62")

# How to add  key-value pairs to an empty dictionary
# Create an empty dictionary
student5 = {}

# Add key-value pairs to it
student5["name"] = "Goodness"
student5["Interest"] = "AI"
student5["Track"] = "AI_Dev"

print(student5)

# List of dictionaries - Each student has their own dictionary
students6 = [
    {"Name": "John", "Interest": "AI", "Track": "AI_Dev"},
    {"Name": "Mary", "Interest": "Cloud Computing", "Track": "AI_Eng"},
    {"Name": "Paul", "Interest": "Cyber Security", "Track": "AI_Dev"}
]

print(students6[0]["Name"])   
print(students6[1]["Track"])  

# Dictionary of dictionaries - Each student is keyed by their ID
students = {
  "AI010"   :  {"Name": "John", "Interest": "AI", "Track": "AI_Dev"},
  "AI020" :  {"Name": "Mary", "Interest": "Cloud Computing", "Track": "AI_Eng"},
  "AI030"  :  {"Name": "Paul", "Interest": "Cyber Security", "Track": "AI_Dev"}
}

print(students7["AI020"]["Name"])   
print(students7["AI030"]["Track"])

# Dictionary of lists - Each subject stores a list of scores
scores3 = {
    "python": [85, 78, 92],
    "pandas": [88, 74, 90],
    "Scikit-learn": [80, 95, 87]
}

print(scores3["python"])    
print(scores3["pandas"][1]) 