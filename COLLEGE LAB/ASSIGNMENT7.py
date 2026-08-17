print("*******************FACTORIAL CALCULATOR*******************")
NUMBER = int(input("Enter the number here:"))


def factorial(n):
    if n < 0:
        return 0
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


print("The factorial of", NUMBER, "is:", factorial(NUMBER))
print("THANKS YOU :-))")