# **Task4: Create a Unique Voters Registration System**

# - Ask for voter names and store in a set.

# - If a voter tries to register twice, display a warning.

# - After registration, display the total number of unique voters.

record = set([])
while True:
    try:
        name = input("Enter your name: ")
        if name in record:
            print("You can\'t register twice na!")
        elif any(char.isdigit() for char in name):          # does not allows numbers. wish i could import 're' to make it restricted to only alphabets.
            print("Ogbon!! Only letters are allowed.")
        elif not name.strip():                              # does not allow empty inputs. Ikr?
            raise ValueError("Input cannot be empty")
        else:
            record.add(name)                                # records the name into the set
        print(f"Total number of voters: {len(record)}")

    except ValueError:
        print("Value Error")                                # i don't like showing the actual error message. users are not techies.
