# # INTRODUCTION TO MODULARITY
# # What is modular programming?
# # modular programming is a way of writing programs by dividing them into smaller,
# # independent, and reusable parts ( modules) instead of writing one long block of code.
# # A module can be a function, a class, or a python file (.py) that performs a specific task.
# # These modules can them be combined to build a complete program.
# # In simple words, modular programming = braking big problems into smaller, manageable solutions.

# # Examples of use here
# # range()
# for i in range(3):
#     print(i) # 0, 1, 2

# # zip()
# names = ["Esther", "Precious", "Kennie"]
# scores = [85, 90, 75]
# for n, s in zip(names, scores):
#     print(n, "scored", s)

# # map()
# nums = [1, 2, 3, 4]
# squared = list(map(lambda x: x**2, nums))
# print(squared) #[1, 4, 9, 16]

# # filter()
# even_nums = list(filter(lambda x: x % 2 == 0, nums))
# print(even_nums) # [2, 4]

# # Take a long look at the code below, please

# # Student Perfomance & Feedback System
# # Step 1: Input student data
# name1 = input("Enter first student name: ")
# score1 = int(input("Enter score for " + name1 + ": "))

# name2 = input("Enter second student name: ")
# score2 = int(input("Enter score for " + name2 + ": "))

# name3 = input("Enter third student name: ")
# score3 = int(input("Enter score for " + name3 + ": "))

# # Step 2: Store in lists
# names = [name1, name2, name3]
# scores = [score1, score2, score3]

# # Step 3: Display data
# print("\nStudent Data:")
# for index, (n, s) in enumerate(zip(names, scores)):
#     print(f"{index + 1}. {n} - {s}")

# # Step 4: Summary using built-ins
# total = sum(scores)
# average = round(total / len(scores), 2)
# highest = max(scores)
# lowest = min(scores)

# print("\nPerformance Summary:")
# print("Total Score:", total)
# print("Total Score:", average)
# print("Average Score:", highest)
# print("Lowest Score:", lowest)

# # Step 5: Ranking (using sorted and zip)
# ranked = sorted(zip(scores, names), reverse = True)
# print("\nRanking:")
# for rank, (score, name) in enumerate(ranked, 1):
#     print(f"{rank}. {name} - {score}")


# # Step 6: Check data types
# print("Data Type Checks:")
# print("Type of names:", type(names))
# print("Type of scores:", type(scores))
# print("ID of names list:", id(names))
# print("ID of scores list:", id(scores))

# # Step 7: Filter passing students (>=50)
# passing = list(filter(lambda s: s >= 50, scores))
# print("\nPassing Scores:", passing)

# # Step 8: Map names to uppercase
# upper_names = list(map(lambda n: n.upper(), names))
# print("Uppercase Names:", upper_names)

# # Step 9: Use help() to show documentation of len
# print("\nHelp on len():")
# help(len)



# # In python, we use the def keyword to define a function. Then we call the function whenever we want to use it.
# # Let's see function structure

# # def function_name(takes in input):
# # process block
# # output block

# # More explanation
# # def function_name(input - here, you will insert an item or list of what the function will need to work):
# # "process block - her will contain the logic or what you want the function to do"
# # " output - Then here will contain what you want the function to output. You can either use the 'return' keyword or 'print()' or 'yield'"

# # defining a function
# def greet():
#     print("Hello, welcome to AI Fellowship!")

# # When you want to use a function, this is how to call it.
# # And you can call it as many times as possible.
# greet()
# greet()
# greet()

# # FUNCTION ARGUMENTS AND PARAMETERS
# # Arguments are variables you add inside the function parenthesis when defining the function (placeholders). Sometimes, they can be optional.
# # Parameters are the actual values you pass inside the function parenthesis when calling the function.

# # Function with an argument - the placeholder
# def greet(name):
#     print("Hello", name, "welcome to Python learning!")

# # Calling with parameter - the actual name
# greet("Class rep")
# greet("Ridwan")

# # When to use return, print(), and yield keywords inside a function
# # print()
# def greet(name):
#     print("Hello", name)

# # Function call
# result = greet("Esther")

# # You will notice that it did not store the name
# print("Result:", result)

# # return
# def add(a, b):
#     return a + b
# # Function call

# result = add(4, 6)
# print("The sum is:", result)
# # Note the output and compare it with that of print()


# # yield
# # This is used for producing a sequence (Generators)
# # yield works like return, but instead of ending the function, it pauses it and remembers its state.
# # Next time you call it, it resumes from where it stopped.
# # This creates a generator.
# # You can use it when working with large data or infinite sequences.

# def count_up_to(n):
#     i = 1
#     while i <= n:
#         yield i # pause and return i
#         i += 1
# # Using the generator
# for number in count_up_to(5):
#     print(number)
# # Note the output: Instead of giving all numbers at once, the function yields them one at a time.


# # Types of arguments
# # POSITIONAL ARGUMENTS
# # these are the most common.
# # the order matters
# # think of it like lining up children in the same order as roll call.
# def introduce(name, track):
#     print("My name is", name)
#     print("I am learning", track, ".")
# # function call
# introduce("Ngozi", "AI Engineering") # Correct order
# # Change the arrangement and watch the output
# introduce("AI Engineering", "Ngozi")    # Incorrect order, this will throw a semantic error

# # KEYWORD ARGUMENTS
# # here you explicitly assign the parameter name when calling the function.
# def introduce(name, track):
#     print("My name is", name)
#     print("I am learning", track, ".")
# # function call
# introduce(name = "Ngozi", track = "AI Engineering")
# # Change the arrangement and watch the output
# introduce(track = "AI Engineering", name = "Ngozi") 

# DEFAULTS ARGUMENTS
# here, you can give parameters a default value.
# even if no value is provided when calling, the default is used.
def introduce(name, track = "AI Engineering"):
    print("My name is", name)
    print("I am learning", track, ".")

# function call
# Without specifying the default argument, but watch the output
introduce("Paul")
# Specify the default argument and watch the output
introduce("Tunji Paul", "AI Development")

# VARYING LENGTH ARGUMENTS
# single asterisk for non-keywords arguments or tuple(*args)
# double asterisk for keyword arguments or dictionary(**kwargs)

# *args(tuple)
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    print("Sum:", total)

# function call
# Take note of the output
add_numbers(2, 4, 6)
add_numbers(10, 20, 30, 40, 50)

# **kwargs(dictionary)
def student_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

# function call
student_details(name="Peter", track = "AI Engineering", interest = "Blockchain")

# implement on full code
#  Define student profile function
# Ensure to note the order of arrangement of the types of arguments used.
# This is how to arrange it if you are using everything or some of them together,

def participant_profile(name, age, track = "AI Development", *skills, **extra_info):
    """
    Generate a profile for a bootcamp participant using different types of arguments.
    """
    profile = f"\n--- Bootcamp Participant Profile ---\n"
    profile += f"Name: {name}\n"
    profile += f"Age: {age}\n"
    profile += f"Track: {track}\n"

    # Skills (from *args)
    if skills:
        profile += "Skills" + ", ".join(skills) + "\n"
    else:
        profile += "Skills: Not yet specified\n"
    
    # Extra info (from **kwargs)
    if extra_info:
        profile += "Additional Info:\n"
        for key, value in extra_info.items():
            profile += f" - {key.capitalize()}: {value}\n"
    return profile
