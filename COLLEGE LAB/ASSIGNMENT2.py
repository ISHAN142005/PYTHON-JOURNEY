n = int(input("How many numbers do you want to check? "))

for _ in range(n):
    num = int(input("\nEnter an integer: "))

    if num > 0:
        print("This number is positive.")
    elif num < 0:
        print("This number is negative.")
    else:
        print("This number is zero.")

    if num % 2 == 0:
        print("This number is even.")
    else:
        print("This number is odd.")
