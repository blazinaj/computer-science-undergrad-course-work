# creates a list of consecutive numbers (1,2,3,4,5..) between 1 and 13 inclusive
def listConsecutiveNumbers (start=1, end=14):
    res = []
    for number in range(start, end, 1):
        res.append(number)
    return res

# sum all of the elements inside of the list
def sumList (list):
    res = 0
    for number in list:
        res += number
    return res

# multiplies all of the elements inside of the list
def multiplyList (list):
    res = 1
    for number in list:
        res *= number
    return res

# prints out even numbers from a list
def printEvenNumbers (list):
    for number in list:
        if number % 2 == 0:
            print(number, end=",")

# Call My cool custom functions
list = listConsecutiveNumbers()

print("Sum total: ", sumList(list))
print("Multiply total: ", multiplyList(list))
printEvenNumbers(list)

