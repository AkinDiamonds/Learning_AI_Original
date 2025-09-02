"""
A to-do list application is a practical project that
 helps users manage tasks efficiently. This application allows
 users to add, remove, and view tasks while keeping track of
 completed and pending activities. Learning to build a to-do
 list enhances understanding of data structures, file
 handling, and basic user interaction in Python.
 This project will cover step-by-step implementation of a to
do list application, user input handling, list operations, and
 file handling for persistent storage.

 Key Concepts of To-Do List in Python
 Basic List Operations:
 -Adding tasks
 -Removing tasks
 -Marking tasks as complete
 -Displaying tasks
 -User Input Handling:
 -Using input() function
 -Handling invalid inputs
 File Handling:
 -Storing tasks in a text file
 -Retrieving saved tasks on program
 restart
 Functions in Python:
 -Defining functions for task management
 -Calling functions with user inputs
"""

# Create empty list
# create adding tasks function
# removing tasks function
# marking tasks as complete function
# displaying task


todo = []
completed = []

# adding tasks
def add_task(*tasks):
    tasks = input("Enter the task(s) you want to add: \n")
    todo.append(tasks)
    print("Task(s) added successfully!\n")

# removing tasks
def remove_task(*tasks):
    print(todo)
    if tasks in todo:
        todo.remove(tasks)
        print("Task(s) removed successfully!\n")
    else:
        print("Error! Type task exactly as displayed in todo list.\n")

# mark as complete function
def mark_task(*tasks):
    print(todo)
    tasks = input("Enter the task(s) you want to mark as complete: \n")
    if tasks in todo:
        todo.remove(tasks)
        completed.append(tasks)
        print("Marked as completed!\n")
    else:
        print("Error! Type task exactly as displayed in todo list.\n")

# display todo list
def display_todo(todo):
    if todo:
        for sn, task in enumerate(todo, start=1):
            print(f"Todo List\n{sn}\t{task}\n")
    else:
       print("No Tasks Yet")

# display completed tasks
def display_completed(completed):
    if completed:
        for sn, task in enumerate(completed, start=1):
            print(f"Completed Tasks:\n{sn}. {task}\n")
    else:
        print("No Completed Tasks Yet")

while True:
    welcome = input('Welcome! What do you want to do today?\n' \
    'Type in a corresponding number:\n' \
    '1. Add a task.\n' \
    '2. Remove a task.\n' \
    '3. Mark task as completed.\n' \
    '4. View pending tasks\n' \
    '5. View completed tasks.\n' \
    '6. Exit\nType here: ')

    if welcome == '1':
        add_task()
    elif welcome == '2':
        remove_task()
    elif welcome == '3':
        mark_task()
    elif welcome == '4':
        display_todo(todo)
    elif welcome == '5':
        display_completed(completed)
    elif welcome == '6':
        print("Bye for now!\n")
        break
    else:
        print("Invalid choice! Please select a valid option.")