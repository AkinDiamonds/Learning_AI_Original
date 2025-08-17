# name organizer
names = input("Enter 5 names (separated by spaces): ") # ask for names
small_lettered_names = names.lower() # change to lowercase
list_of_names = small_lettered_names.split() # change to a list of words
sorted_names = sorted(list_of_names) # sort alphabetically
for x in sorted_names: # highlight each word in the list
    print(x) # display