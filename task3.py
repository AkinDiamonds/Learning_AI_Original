# **Task3: Days and Activities Pairing**
# - Store days of the week in a tuple and ask the user
#  to input an activity for three specific days.

#   - Use dictionary comprehension to pair days and activities.

#   - Print the dictionary.

# - Requirements:

#   - Use a tuple for days.

#   - Use {day: activity for day, activity in `zip(..., ...)`}.
#   Tip: Research on how to use `zip()`

days = ("Sunday","Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
activity1 = input(f"Type an activity for {days[0]}: ")
activity2 = input(f"Type an activity for {days[1]}: ")
activity3 = input(f"Type an activity for {days[2]}: ")
activities = [activity1, activity2, activity3]
days_activity ={day: activity for day, activity in zip(days, activities)}
print(days_activity)