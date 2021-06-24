"""
Author: Jacob Blazina
Date: 6/21/2021
File: AverageExamScoresCalculator.py
Title: Lab 3
"""

# Initialize variables
sum_elements = 0
average_score = 0

scores = []

# Allow user to enter exam scores until they decide to stop
while 1 > 0:
    user_input = eval(input("Enter an exam score or -1 to stop: "))
    if user_input == -1:
        break
    else:
        scores.append(user_input)

# Print the scores. Doing this in two separate loops due to the lab instructions
print("The exam scores:")

for score in scores:
    print(score, end=",")

for score in scores:
    sum_elements += score

# Calculate the average score
average_score = sum_elements / len(scores)

# Print the average score
print()
print("The average exam score is: " + str(average_score))
