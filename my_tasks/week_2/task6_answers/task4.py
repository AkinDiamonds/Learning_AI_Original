# **Task4: Create a Unique Voters Registration System**

# - Ask for voter names and store in a set.

# - If a voter tries to register twice, display a warning.

# - After registration, display the total number of unique voters.

record = set([])
while True:
    name = input("Enter your name: ")
    if name in record:
        print("You can\'t register twice na!")
    else:
        record.add(name)
    print(f"Total number of voters: {len(record)}")
