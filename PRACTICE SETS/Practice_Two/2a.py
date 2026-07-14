# Create a program that checks the person is eligible to vote or note(age>18)

try:
    age = int(input("Enter your age here:"))
    print("Entered age is:", age)

    if age < 0:
        print("Not possible!")
    elif age < 18:
        print("Not eligible to Vote!")
    else:
        print("Eligible to Votr! :-)")
except ValueError:
    print("Invalid Input!")

print("ThankYou")
