# Write a function full_name(first, last) that takes first name and last name as parameters and returns a single string in the format "First Last".


def full_name(first, last):
    return f"{first} {last}"


fname = input("Enter your first name here:")
lname = input("Enter your last name here:")
print("Full name is:", full_name(fname, lname))
