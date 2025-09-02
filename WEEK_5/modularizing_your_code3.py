# Key Rules
# init always take self as first parameter
# All methods take self as first parameter
# Never pass self manually when calling methods
# Use self inside methods to access object's attributes
# self refers to the specific object being used

# class Student:
#     def __init__(self, name, course, level): # This runs automatically
#         print("Creating a new student...")
#         self.name = name
#         self.course = course
#         self.level = level
#         print(f'Student {name} has been created!')

# # When you create a student, __init__ runs automatically
# kemi = Student("Kemi Adebayo", "Computer Science", 300)

# # How init and self work together

# class NigerianStudent:
#     def __init__(self, name, state, course):
#         print(f"Step 1: Creating student object...")
#         self.name = name    # Step 2: Assign name to this object
#         self.state_of_origin = state    # Step 3: Assign state to this object
#         self.course = course    # Step 4: Assign course to THIS object
#         self.student_id = self.generate_id()   # Step 5: Generate ID for THIS object
#         print(f"Step 6: {self.name} from {self.state_of_origin} is ready")

#     def generate_id(self):
#         import random
#         return f"UNISAIL{random.randint(1000, 9999)}"
        

# ayo = NigerianStudent("Ayo Daniel", "Lagos", "Street Statistics")

# print(ayo.name)
# print(ayo.student_id)


#  a class that collects name and network and writes that lagbaja joined tamedo network
# and can buy airtime

# class Phone_contact:
#     def __init__(self, name, network):
#         self.name = name
#         self.network = network
#         self.balance = 0
#         # print(f"{self.name} has joined {self.network} network!")
    
#     def buy_airtime(self, amount):
#         self.balance += amount
#         return f"{self.name} has bought {amount} airtime. Balance: {self.balance}"

# simeon = Phone_contact("Simeon Akinrinola", "MTN")
# abeeb = Phone_contact("Abeeb Bakare", "Airtel")

# print(simeon.name.upper())
# print(abeeb.name.center(1))
# print(simeon.buy_airtime(500))
# print(abeeb.buy_airtime(300))
# print(simeon.balance)
# print(abeeb.balance)

# Defining Attributes of a student
# class Student:
#     university = "Federal University of Agriculture Abeokuta"
#     def __init__(self, name, course, level, state_of_origin):
#         self.name = name
#         self.course = course
#         self.level = level
#         self.state_of_origin = state_of_origin
#         self.cgpa = 0.0

# Creating a student object
# Fathia = Student("Fathia Balogun", "Theatre Art", f"{300}l", "Ogun State")
# print(Fathia.course)
# print(Fathia.name)
# print(Fathia.level)
# print(Fathia.state_of_origin)

# Types of Attributes
# 1. Instance Attributes - Unique to each object

# student1 = Student("Anthony Joshua", "Engineering", 200, "Ogun")
# student2 = Student("Fadilat Hassani", "Medicine", 400, "Lagos")

# print(student1.name)
# print(student2.name)
# print(student2.university)
# print(student1.university)

# METHODS
# class Student:
#     university = "Federal University of Agriculture, Abeokuta."
#     def __init__(self, name, course, level):
#         # Attributes
#         self.name = name
#         self.course = course
#         self.level = level
#         self.cgpa = 0.0
#         self.fees_paid = False

#     # Method: action the student can do
#     def pay_school_fees(self):
#         self.fees_paid = True
#         return f"{self.name} has paid school fees for {self.level} level"
    
#     # Method: another action
#     def register_courses(self):
#         if self.fees_paid:
#             return f"{self.name} has successfully registered courses for {self.course}"
#         return f"{self.name} must pay school fees first!"
#     # Method: calculates CGPA
#     def calculate_cgpa(self, grades):
#         if grades:
#             self.cgpa = sum(grades) / len(grades)
#             return f"{self.cgpa:.2f}"
#         return f"No grades provided!"
    


# There are instance methods, class methods and static methods.
# Instance methods uses self and are specific to the object currently in use

# Class Methods - Work with class-level data
# calls data not specific to self attributes
#     @classmethod
#     def get_university(cls):
#         return cls.university
    
#     @staticmethod
#     def academic_calendar():
#         return "Academic session runs from September to July"
    
# simeon = Student("Simeon Akinrinola", "AI Development", 300)

# print(simeon.cgpa)
# print(simeon.course)
# print(simeon.pay_school_fees())
# print(simeon.fees_paid)
# print(simeon.register_courses())
# print(simeon.calculate_cgpa([100, 100, 100, 100, 100, 100]))
# print(simeon.get_university())
# print(simeon.academic_calendar())


# Static methods 
# They do not need object or class data at all.
# They return a response of their own.
# You need to specify @staticmethod before you define

# How attributes and methods work together

# the class has methods that deposits, withdraws, transfers, checks
#  balance and generates account number

# class bankAccount:
#     def __init__(self, owner, bank_name, balance=0):
#         # ATTRIBUTES
#         self.owner = owner
#         self.bank_name = bank_name
#         self.balance = balance
#         self.account_number = self.generate_account_number()
    
#     # METHODS
#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             return f"{self.owner} has deposited {amount} into their {self.bank_name} account."
#         else:
#             return "No amount entered"
    
#     def withdraw(self, amount):
#         if amount > 0 <= self.balance:
#             self.balance -= amount
#             return f"{self.owner} has withdrawn {amount} from their {self.bank_name} account."
#         return "No amount entered"
    
#     def transfer(self, Recipient, amount):
#         if Recipient and amount:
#             self.balance -= amount
#             return f"{self.owner} has transfered {amount} from their {self.bank_name} account to {Recipient}"
#         return "No Recipient or amount entered"
    
#     def check_balance(self):
#         return f"Your balance is {self.balance}"
    
#     def generate_account_number(self) -> int:
#         import random
#         return f"Your account number is: 06{random.randint(10000000, 99999999)}"
    
    




# simeon = bankAccount("Simeon Akinrinola", "UBA")
# print(simeon.deposit(5000000000))
# print(simeon.balance)
# print(simeon.generate_account_number())
# print(simeon.withdraw(2000000))
# print(simeon.check_balance())


# write a class that simulates a phone
#  in naija. the phone can poweron, buy airtime, make call, send sms
class NaijaPhone:
    def __init__(self, owner, network):
        self.owner = owner
        self.network = network
        self.airtime_balance = 0
        self.power_on = False

    def power_on(self):
        self.power_on = True
        return f"{self.owner}'s phone is on!"
    
    def buy_airtime(self, amount):
        if amount and amount > 0:
            self.airtime_balance += amount
            return f"{self.owner}'s has successfully bought N{amount} airtime"
        return "Invalid amount!"
    
    def make_call(self, contact):
        if contact and self.airtime_balance >= 4:
            self.airtime_balance -= 4
            return f"{self.owner} is calling {contact}"
        elif not self.power_on:
            return "Power off!"
        return "Insufficient Balance or No Contact Entered"
    
    def send_sms(self, contact):
        if contact and self.airtime_balance >= 6:
            return f"{self.owner} sent an SMS to {contact}"
        elif not self.power_on:
            return "Power off!"
        return "Insufficient Balance or No Contact Entered"