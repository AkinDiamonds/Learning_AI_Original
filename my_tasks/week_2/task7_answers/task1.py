# **Task1: Student Bio Data Storage**

# - Create a program that collects student bio-data from user input (name, age, gender, courses) and stores it in a dictionary.

#   - Courses should be stored as a list.

#   - Display the bio-data neatly using escape sequences.

# - Requirements:

#   - Use `input()` to collect details.

#   - Use dictionary operations `(dict[key] = value)` to store data.

#   - Use `print()` formatting with `\n` and `\t` for better output.


name = input("Enter your name: ")
age = input("Enter your age: ")
gender = input("Enter your gender: ")
courses = input("Enter your courses(separated by spaces): ")
courses_split = courses.split()
courses_join = ", ".join(courses_split)
storage = {"Name": name, "Age": age, "Gender": gender}
print('Student\'s Bio Data Loading:\n' \
    f'Name:\t {storage["Name"]}\n' \
    f'Age:\t {storage["Age"]}\n' \
    f'Gender:\t {storage["Gender"]}\n' \
    f'Courses: {courses_join}'
)