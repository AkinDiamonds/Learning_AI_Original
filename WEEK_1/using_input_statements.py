# Basic usage of input()
'''
name = input("Enter your name: ")
print("Hello, ", name)

# Convert input to integer
age = int(input("Enter your age: "))
print(f"You will be {age + 1} years old next year.")

# Welcome customer and ask what they will eat in my restaurant.
# Step 1: Defined variable (i.e order).
# Step 2: Variable is an input in string format
# Step 3: Print message using f-string, \n, and the variable.
order=input("What would you like to eat today?: ")
print(f"Welcome to Simeon's Restaurant!\nKindly wait 2 mins as your {order} is being prepared")

# Calculator using input
num1 = float(input("Enter first number: ")) #assign first variable
num2 = float(input("Enter second number: "))    # Assign second variable
sum_result = num1 + num2    # Sum of first and second variables
print(f"The sum of {num1} and {num2} is {sum_result}.") # Print result
'''

# ATM Machine Withdrawal
# Welcome
# Ask for name
# Request PIN
# Request Amount
# Print Successful Withdrawal and declare Remaining Account Balance

Name = input("Welcome! Please Enter Your Name: ")
Account_Balance = float(2507570.97)
PIN = int(input("Enter Your PIN: "))
Amount = int(input("Amount to withdraw: "))
print(
    f"\n\nYou have successfully withdrawn {Amount}\nAccount Balance: {Account_Balance -Amount}\n\nThank you for banking with us, {Name}." 
)