# Task3: Simulate a football match ticket system**

# - Store all seat numbers (1 to 50) in a set.

# - Ask users to "book" a seat by entering the number.

# - Remove booked seats from the set.

# - Show remaining seats after each booking.

# create a set: seats using range
# assign book_number to user's input
# use while loop to define condition
# use if condition in while loop to keep input in range
# print seats and ask input

seats = set(range(1, 51))
book_number = int(input("Enter a number from 1 to 50: "))
while book_number > 0:
    if book_number in seats:
        seats.remove(book_number)
    else: print("Ticket number is not available.")
    print(seats)
    book_number = int(input("Enter a number from 1 to 50: "))

