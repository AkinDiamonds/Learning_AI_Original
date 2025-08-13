# student score tracker
new_student_names = (input("Enter 3 students names: ").split()) # get input as string and change to list
score1 = input(f"Enter {new_student_names[0]}\'s score: ") 
score2 = input(f"Enter {new_student_names[1]}\'s score: ")
score3 = input(f"Enter {new_student_names[2]}\'s score: ")
new_scores=score1 + score2 + score3 # concatenate scores into a new list

#print score table
print(f"{new_student_names[0]}\t", f'{new_scores[0]}\n'
      f"{new_student_names[1]}\t", f'{new_scores[1]}\n'
      f"{new_student_names[2]}\t", f'{new_scores[2]}\n')