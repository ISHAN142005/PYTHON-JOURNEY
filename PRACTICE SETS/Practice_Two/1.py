# WAP that asks the user for a number and prints whether it is positive negative or zero.
num = int(input("Enter the number here:"))
print("Entered number is:", num)
if num > 0:
    print("Entered number is positive!")
elif num < 0:
    print("Entered number is Negative!")
else:
    print("Entered number is Zero!")
print("Thank You:-)")
