# creating a contact quick lookup
# collect names and phone in tuple
# create dictionary
# ask for input
# print using .get() for safe retrieval

names = ("Simeon", "Akin", "Ola")
phone =  ("08012345678", "07098765432", "09011010011")
set_of_names = {name: phones for name, phones in zip(names, phone)}
enter_name = input("Enter a name from among these: Simeon, Akin, Ola: ").title()
print(set_of_names.get(enter_name, "Not Found!"))
