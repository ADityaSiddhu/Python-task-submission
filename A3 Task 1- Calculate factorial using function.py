#Assignment 3:
#Task 1: Calculate Factorial using function

num = int(input("Enter a Number: "))

def factorial(num):
    if num < 2:
        return 1
    else:
        return num * (factorial(num-1))

result = factorial(num)
print("Factorial of",num,"is", result)