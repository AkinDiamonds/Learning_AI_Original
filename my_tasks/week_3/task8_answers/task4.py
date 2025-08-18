# create dictionary
student = dict()

# student's info
name = input("Enter your name: ").title()
age = int(input("Enter your age: "))
student["Name"] = name
student["Age"] = age

# scores
scores = [90, 85, 70, 80]
student["Scores"] = scores

# check if student passed
passed = (sum(scores) // len(scores)) >= 50
student["Passed"] = passed

# check if student is a teenager
teenager = (age > 13) and (age < 19)
student["Teenager"] = teenager

# display
print(f"Student Record:\nName: {student['Name']}\nAge: {student['Age']}\n\
Scores: {student['Scores']}\nPassed: {student['Passed']}\nTeenager: {student['Teenager']}")
