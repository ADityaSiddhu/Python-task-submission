## Assignment 5
# Task 1: Create a Dictionary of Student Marks
try:
    marks = {"Alice":85, "Aditya":75, "Deepti":94, "Fizaa":92}
    key = input("Enter the student's name: ")

    print("{}'s marks: ".format(key),marks[key])
except KeyError:
    print("No student with this name, pls check again.")