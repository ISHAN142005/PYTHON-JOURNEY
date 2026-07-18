"""
Write a function safe_divide(a, b) that returns the result of a / b, but returns "Cannot divide by zero" if b is 0.
"""


def safe_divide(a, b):
    if b == 0:
        return "Cannot divide by zero"

    return a / b


num1 = int(input("Enter the first number here:"))
num2 = int(input("Enter the second number here:"))

print("The resultant of", num1, "/", num2, "is:", safe_divide(num1, num2))
