"""
Author: Jacob Blazina
Date: 6/21/2021
File: Cars.py
Title: Lab 2 - Part 1
"""

# Declare makes, models, and years
makes = [
    "Honda",
    "Toyota",
    "Mercedes",
    "Ford"
]

models = [
    "Accord",
    "Camry",
    "C63AMG",
    "F150"
]

years = [
    2001,
    1989,
    2019,
    2020
]

# Adjust year and model
years[1] = 2019
models[3] = "F350"

# Add new car
makes.append("BMW")
models.append("M6")
years.append(2009)

for i, make in enumerate(makes):
    print("Car ", i + 1, " :", years[i], " ", makes[i], " ", models[i])
