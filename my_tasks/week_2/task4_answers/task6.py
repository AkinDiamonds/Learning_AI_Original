# word analyzer
word = input("Enter a Word: ")
uppercase = word.isupper()
lowercase = word.islower()
titlecase = word.istitle()
print("Analyzing your word...\n" \
"Done!")
print("Length of your word is: ", len(word))
print(f"Uppercase: ", uppercase)
print("Lowercase: ", lowercase)
print("Titlecase: ", titlecase)
print("Your word in reverse: ", word[::-1])