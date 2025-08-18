# create dictionary: student
student = dict()

# student's info
age = int(input("Enter your age: "))
utme_score = int(input("Enter your UTME score: "))
first_choice = input("Enter your first choice university(e.g. UNILAG, FUNAAB, etc.): ").upper()
o_level = input("Did you have at least 5 credit passes in relevant O'Level subjects including Maths and English?[Yes/No]: ").title()
o_level_sitting = int(input("Enter number of sitting(s) for your O'Level(e.g. 1, 2, etc.)"))
post_utme = input("Did you participate in UNILAG's online Post-UTME screening?:[Yes/No] ").title()
post_utme_score = int(input("Enter your Post-UTME score: "))

# store in "student"
student["Age"] = age
student["UTME Score"] = utme_score
student["First Choice University"] = first_choice
student["Five (5) Credit passes in relevant O'Level subjects"] = o_level == "Yes"
student["Number of O'Level sittings"] = 1
student["Did UNILAG's Post-UTME"] = post_utme == "Yes"
student["Post-UTME score"] = post_utme_score

# departmental cut-off mark calculation
dep_cutoff = (age >= 16) and (((utme_score + post_utme_score) / 500) * 100) >= 50

# display
print(f"Student's Eligibility Check\n\
Age: {age}\n\
UTME Score: {student['UTME Score']}\n\
First Choice University: {student['First Choice University']}\n\
Five (5) Credit passes in relevant O'Level subjects: {student['Five (5) Credit passes in relevant O\'Level subjects']}\n\
Number of O'Level sittings: {student['Number of O\'Level sittings']}\n\
Did UNILAG's Post-UTME: {student['Did UNILAG\'s Post-UTME']}\n\
Post-UTME score: {student['Post-UTME score']}\n\n\
Eligible for Admission: {dep_cutoff}")