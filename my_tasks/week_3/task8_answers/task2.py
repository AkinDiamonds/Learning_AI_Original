# Candidate's Info
name = input("Enter your name: ")
age = int(input("Enter your age: "))
score = int(input("Enter your test score: "))

# eligibility calculation
eligibility = (age < 18) and (score > 70)
# print(f"Candidate: {name}\nAge: {age}\nScore: {score}\nEligible: {eligibility}")

'''The code collects user's input, stores in variables 
and uses operators to calculate user's eligibility'''

# Candidate's Scholarship Info
citizen = input("Are you a citizen of Nigeria?[Yes/No]: ").title()
undergrad = input("Are you currently a full-time undergraduate student in recognized Nigerian university?[Yes/No]: ").title()
other_scholarship = input("Are you currently receiving any other scholarship from an entity in the Oil and Gas industry, " \
"whether national or international?[Yes/No]: ").title()
qualification = input("Do you have at least 5 distinctions(As and Bs) in relevant subjects in your WAEC/WASSCE(May/June) exams," \
" including English and Mathematics?[Yes/No]: ").title()

# eligibility calculation
eligibility2 = (age < 18) and (score > 70) and (citizen == "Yes") and (undergrad == "Yes") and (other_scholarship == "No") and (qualification == "Yes")
print(f"Candidate: {name}\nAge: {age}\nScore: {score}\nEligible for scholarship: {eligibility2}")