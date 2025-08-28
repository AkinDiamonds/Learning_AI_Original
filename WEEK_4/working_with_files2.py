# setting up: it's cleaner to work inside a folder so files don't clutter desktop

# from pathlib import Path

# workspace = Path("workspace_files")
# workspace.mkdir(exist_ok=True)
# file_path = workspace / "notes.txt"
# print(file_path.cwd())

# # Create file

# # (A) Create or overwrite using 'w'
# f = open(file_path, "w", encoding="utf-8")
# f.write("This is the first line in notes.txt\n")
# f.close()

# # # (B) Safe-create using 'x' (uncomment to try once)
# # f = open(file_path, "x", encoding="utf-8")
# # f.write("This is the first line in notes.txt.\n")
# # f.close()

# # open a file
# # open for writing again (this will overwrite!)
# f = open(file_path, "w", encoding="utf-8")
# f.write("Replaced the old content with this line.\n")
# f.close()

# # write to file
# f = open(file_path, "w", encoding="utf-8")
# f.write("Shopping List:\n")
# f.write(" - Rice\n")
# f.write(" - Beans\n")
# f.write(" - Garri\n")
# f.close()

# # Append to a file
# f = open(file_path, "a", encoding="utf-8")
# f.write(" - Groundnut oil\n")
# f.write(" - Maggi\n")
# f.close()

# # Read from a file
# # there are four common ways:
# # read() - whole file as one string
# # read(n) - first n characters
# # readline() - one line
# # readlines() - a list of all lines

# # read the whole file
# f = open(file_path, "r", encoding="utf-8")
# content = f.read()
# f.close()
# print(content)

# # read line by line
# f = open(file_path, "r", encoding="utf-8")
# print("First line:", f.readline().rstrip())
# print("Second line:", f.readline().rstrip())
# f.close()

# # read as a list of lines
# f = open(file_path, "r", encoding="utf-8")
# content = f.readlines()
# f.close()
# print([line.rstrip() for line in content])

# #  Iterate over lines (memory friendly)
# f = open(file_path, "r", encoding="utf-8")
# for line in f:
#     print("->", line.rstrip())
# f.close()

# # the best practice is to use With open(...) as f:
# # the with statement automatically closes the file even if an error  happens. This is the recommended way.

# #  write safely
# with open(file_path, "w", encoding="utf-8") as f:
#     f.write("My Todo List:\n")
#     f.write(" - Revise Python file handling\n")
#     f.write(" - Practice error handling within a function")
#     f.write(" - Practice JSON & CSV\n")

# # Append safely
# with open(file_path, "a", encoding="utf-8") as f:
#     f.write(" - Build a small project\n")

# # Handling errors related with files

# from pathlib import Path
# workspace = Path("workspace_files")
# workspace.mkdir(exist_ok=True)

# # Try to read a file that doesn't exist
# try:
#     with open(workspace / "missing_file.txt", "r") as f:
#         content = f.read()
#         print("File content:", content)
# except FileNotFoundError:
#     print("Oops! That file doesn't exist yet.")
#     print("Let's create it first!")

# #  Now create the file
#     with open(workspace / "missing_file.txt", "w") as f:
#         f.write("Now the file exists!")
#     print("File created successfully")

# # before trying to read or write files, it's smart to check if they exist first.

# #  import Path
# # create a path to workspace and notes.txt
# # check if the file exists
# # if it exists, get file name, size and show it's contents
# # if it doesn't exist, say it doesn't exist


# from pathlib import Path

# workspace = Path("workspace_files")
# file_path = workspace / "notes.txt"

# if file_path.exists():
#     print("File Name:", file_path.name, '\n')
#     print("File Size:", file_path.stat().st_size, "Bytes\n")

#     with open(file_path, "r") as f:
#         print("File Content:\n", f.read())
# else:
#     print("This file does not exist!")


# WORKING WITH JSON FILES (STORING DATA)

# import json
# import path
# create path to "workspace_files"
# create a database containing a student's data
# save the data to a JSON file
# read the data back
# print the data and python grade

import json
from pathlib import Path

workspace = Path("workspace_files")
json_file = workspace / "json_file"

student_data = {"Name": "Simeon Akinrinola",
                "Track": "AI Development",
                "Seat Number": 142,
                "Courses": {"Python": "A", "MLOPS": "A", "Design": "A", "Logic": "A"},
                "Is Graduated": True}

# save to json
with open(json_file, "w", encoding="utf-8") as f:
    json.dump(student_data, f, indent=2)

# read the data
with open(json_file, "r", encoding="utf-8") as f:
    content = json.load(f)

print("\nName:", content["Name"], "\n"
      "Track:", content["Track"], "\n"
      "Seat Number:", content["Seat Number"], "\n"
      "Python Grade:", content["Courses"]["Python"], "\n"
      "Graduated:", content["Is Graduated"], "\n")