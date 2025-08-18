num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"{num1} == {num2} : {num1 == num2}")
# Input: num1 = 4, num2 = 5.
# Output: 4 == 5 : False. 
# The code collects user's inputs(numbers) and checks if both inputs are equal. In the above case, it returned False. because 4 is not equal to 5.

print(f"{num1} != {num2} : {num1 != num2}")
# Input: num1 = 4, num2 = 5.
# Output: 4 != 5 : True. 
# In this case, 4 is not equal to 5 (4 != 5). Hence, the output returns True.

print(f"{num1} > {num2} : {num1 > num2}")
# Input: num1 = 4, num2 = 5.
# Output: 4 > 5 : False. 
# In this case, 4 is not greater than 5. Hence, the output returns False.

print(f"{num1} < {num2} : {num1 > num2}")
# Input: num1 = 4, num2 = 5.
# Output: 4 < 5 : True.
# In this case, 4 is less than 5. Hence, the output returns True.

# Use case 1: Determining whether a student passed the class.
# Use case 2: Determining whether a user's number is among the winning lottery number.
# Use case 3: Determining whether a user's heart rate is healthy.

# Code for Use case 1:

# pass mark
pass_mark = 45

# student's input
score = int(input("Enter your overall score: "))

# determine Pass or Fail
print(f'Passed Class: {score > pass_mark}')
