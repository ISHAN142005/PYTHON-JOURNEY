# Write a recursive function factorial(n) that returns the factorial of a number.


def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


num = int(input("Enter the number here:"))
print("The factorial of", num, "is:", factorial(num))
