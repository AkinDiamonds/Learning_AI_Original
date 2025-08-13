# **Task 7: List Manipulation**
# - Create a list of five cities.

# - Replace the third city with a new one (entered by the user).

# - Remove the last city.

# - Add a new city to the beginning of the list.

# - Print the updated list.
cities = ["Lagos", "Abeokuta", "Ibadan", "Tokyo", "Texas"]
cities.remove("Ibadan")
cities.insert(2, input("Enter your city: "))
print(cities)
cities.remove ("Texas")
cities.insert(0, "Moscow")
print("Updated list: ", cities)