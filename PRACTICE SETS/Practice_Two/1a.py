# WAP that asks the user for a number and prints whether it is positive, negative, or zero.

try:
    num = int(input("Enter the number here: "))
    print("Entered number is:", num)

    if num > 0:
        print("Entered number is Positive!")
    elif num < 0:
        print("Entered number is Negative!")
    else:
        print("Entered number is Zero!")

except ValueError:
    print("Invalid input! Please enter a valid integer.")

print("Thank You :-)")
