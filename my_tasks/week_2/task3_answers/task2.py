# Write a program to take a string input from the user and display it in uppercase.
given = "Python is a programming language"
print("python" in given.lower())

# Write a program to reverse a string without using slicing ([::-2])
string = "Python"
print("".join(reversed(string)))

# Given a string with extra spaces, remove the leading and trailing spaces.
string = "      Python is a programming language        "
print(string.strip())

# Ask the user for a sentence and print the number of vowels in it.
sentence = input("Enter a sentence: ").lower()
print(sentence.count("a") + sentence.count("e") + sentence.count("i") + sentence.count("o") + sentence.count("u"))

# Convert a string "1234" to an integer and multiply by 2.
string = "1234"
converted_string = int(string) * 2
print(converted_string)