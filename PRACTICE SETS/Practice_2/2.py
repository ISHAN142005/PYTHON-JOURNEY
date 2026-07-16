# Create a program that checks the person is eligible to vote or note(age>18)

age = int(input("Enter your age here:"))
print("Entered age is:", age)

if age >= 18:
    print("You are eligible to vote!")
elif age < 18:
    print("You are not eligible to vote!")
else:
    print("Invalid Input!")

print("Thank You:-)")
