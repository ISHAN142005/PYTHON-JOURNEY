# WAP that takes input from the user and tells whether it is even or odd

try:
    num = int(input("Enter your number here:"))
    print("Entered number is:", num)
    if num == 0:
        print("Zero is neither even nor odd!")
    elif (num % 2) == 0:
        print("Enter number is a Even Number!")
    else:
        print("Entered number is a Odd Number!")
except ValueError:
    print("Invalid Input!")
