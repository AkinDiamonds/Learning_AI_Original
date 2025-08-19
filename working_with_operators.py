# python operators
# operators are special symbols in python that perfoms operations on variables and values. Here we will focus on:
# comparison  operators
# assignment operators
# logical operators
# comparison operators are used to compare teo values. The result is always True or False.
# == means equal to
# != means not equal to
# > means greater than
# < mean less than
# >= means greater than or equal to
# <= means less than or equal to

a = 10
b = 20
print(a==b) # False
print(a!=b) # True
print(a>b) # False
print(a < b) # True
print(a >= 10) # True
print(a <= 25) # True
# Use case example - student exam result
score = 75
print(score >= 50) # True (Passed)
print(score < 50) # False (Failed)
print(score == 100) # False (Not full marks)

# Assignment operators
# assignment operators are used to assign values to variables. They can also combine an operation with assignment, so instead of writing x = x + 5, we can write x += 5.
# = is an assignment operator
# += adds the following number to the variabe and still assigns it
# -= subtracts from x
# *= multiplies x by the number assigned
# /= divides x by the number assigned
# %= stores remainder after division
# x **=2 raises x to the power of 2
# x //= 2 floor divides x by 2
x = 10
print("Initial value: ", x)
x += 5
print ("After x += 2: ", x)
x -= 2
print("After x -= 2: ", x)
x *= 3
print("After x *= 3: ", x)
x /=4
print("After x /= 4: ", x)
x %= 3
print("After x %= 3: ", x)
x = 4
x **= 2
print("After x //= 3:", x)

# use case example:
# define variables
balance = 1000
deposit = 200
withdraw = 150

balance += deposit # Add deposit
balance -= withdraw # subtract withdrawal

print("Updated Balance: ", balance)
# Output: Updated Balance: 1050

# Logical Operators
# logical operators are used to combine conditional statements. They work with Boolean values (True or False.)
# x > 5 and x < 15 is True if both conditions are true
# x < 5 or x > 20 is True if at least one condition is True
# not(x == 10) is True if the condition is false

x = 10
y = 20

# and operator
print(x > 5 and y > 15) # True
# or operator
print(x < 5 or y > 15) # True
# not operator
print(not(x==10)) # False
# Use case example1 - Scholarship Eligibility
# Define variables
age = 17
score = 85

# Must be  younger than 18 AND score above 80
eligible = (age < 18) and (score > 80)
print("Scholarship Eligible: ", eligible)
# Output: Scholarship Eligible: True

# Use case example2 - Event Access
age = 22
has_ticket = False
can_enter = (age >= 18) and (has_ticket or age < 25)
print("Access Granted:", can_enter)
# Output: Access Granted: True (because age < 25 even without ticket)