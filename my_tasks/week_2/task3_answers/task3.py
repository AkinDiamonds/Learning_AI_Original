# Given "apple, banana, orange", split the string into a list of fruits.
fruits = "apple, banana, orange"
print(fruits.split())

# Ask the user for a sentence and print each word on a new line
word = input("Type a sentence: ").split()
for w in word:
    print(w, end="\n")

# replace all spaces in a string with underscores (_).
sentence = "Python is a programming language"
edited = sentence.split()
print('_'.join(edited))

# count how many times the letter "a" appears in "Banana".
w = "banana"
print(w.count("a"))

# check if a given string starts with "https://"
string = "https://www.ai.com"
print(string.startswith("https://"))