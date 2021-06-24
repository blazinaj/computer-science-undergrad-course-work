"""
Author: Jacob Blazina
Date: 6/21/2021
File: SeasonsAndDays.py
Title: Lab 2 - Part 2
"""

import sys

# Get day number input
day_num = eval(input("Please enter a number between 1 and 7: "))

# Initialize other variables
day = ""
month = ""

# Set the day string based on number input
if day_num == 1:
    day = "Monday"
elif day_num == 2:
    day = "Tuesday"
elif day_num == 3:
    day = "Wednesday"
elif day_num == 4:
    day = "Thursday"
elif day_num == 5:
    day = "Friday"
elif day_num == 6:
    day = "Saturday"
elif day_num == 7:
    day = "Sunday"
else:
    sys.exit()

# Setup Season constants
spring = [
    "Spring",
    "spring",
    "SPRING"
]

summer = [
    "Summer",
    "summer",
    "SUMMER"
]

fall = [
    "Fall",
    "fall",
    "FALL"
]

winter = [
    "Winter",
    "winter",
    "WINTER"
]

# Prompt for season
season = input("What season is it?")

# Handle advanced season/day logic
if season == spring[0] or season == spring[1] or season == spring[2]:
    month = "March"
elif season == winter[0] or season == winter[1] or season == winter[2]:
    month = "December"
elif season == fall[0] or season == fall[1] or season == fall[2]:
    month = "September"
elif season == summer[0] or season == summer[1] or season == summer[2]:
    if day_num <= 3:
        month = "June"
    else:
        month = "July"
else:
    print("Error: Invalid Season", season)
    sys.exit()

# Print the outputs
print("The day is ", day, "which is day number: ", day_num)
print("The Month is ", month, "which is in the season: ", season)

# Optional summer output
if season == summer[0] or season == summer[1] or season == summer[2]:
    if day_num == 6:
        print("Go swimming!")
