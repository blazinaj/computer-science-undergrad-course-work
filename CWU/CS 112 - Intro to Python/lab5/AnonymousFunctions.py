"""
Author: Jacob Blazina
Date: 6/21/2021
File: AnonymousFunctions.py
Title: Lab 5
"""

# Adds 3 numbers together and multiplies by 10
x = lambda a, b, c: (a+b+c)*10

# Adds two numbers together
addTwo = lambda a, b: a + b
print("Add two : ", addTwo(9, 9))

# Averages three numbers
average = lambda a, b, c: (addTwo(a, b) + c)/3
print("Average three : ", average(1, 2, 3))

# Raises a number to the power of 3
powerThree = lambda a: a*a*a
print("Power of three : ", powerThree(5))

# Welcome, to the World of Tomorrow!! 🔮
info = lambda: "Hello World"
print("Info : ", info())

# Strips whitespace and coverts string to lower case
lowerStr = lambda a: a.strip().lower()
print("Lower case string : ", lowerStr(" CWU "))

# Strips whitespace and coverts string to upper case, then substrings index 1:4
subUpperStr = lambda a: a.strip().upper()[1:4]
print("Upper sub string : ", subUpperStr(" ccWucentral"))

# Prints the first half of a list
halfList = lambda a: a[0:(round(len(a) / 2))]
print("First half of the list : ", halfList([1, 2, 3, 4, 5, 6]))

