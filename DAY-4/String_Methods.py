# Strings are immutable
name = "Ishan"
# name[0]='r' #we can't do this!

l = len(name)
print(l)

print(
    "*****************************************************************************************"
)

a = "brand new"
print(a.lower(), a)  # -->  This will lowercase all and a is for seeing that there is no change in original
print(a.upper(), a)  # -->  This will uppercase all
print(a.capitalize(), a)  # -->  This will capitalize the first letter of string
print(a.title(), a)  # -->  This will capitalize the first letter of all word of string

print(
    "*****************************************************************************************"
)


# strip removes leading and trailing whitespaces from a string
print("Stripping")
print(a.strip())
print(a.lstrip())
print(a.rstrip())

print(
    "*****************************************************************************************"
)

# Finding and replacing
print("Finding and replacing")
b = "My name is Ishan."
print(b.find("is"))
print(b.replace("Ishan", "Ishan Bohra"))


print(
    "*****************************************************************************************"
)
# SPLITTING & JOINING

A = "MILK,WATER,JUICE"
fruits = A.split(",")
print(fruits)  # Output: ['MILK', 'WATER', 'JUICE']

new_A = " - ".join(fruits)
print(new_A)  # Output: "MILK - WATER - JUICE"


print(
    "*****************************************************************************************"
)

A = "Python123"
print(A.isalpha())  # Output: False
print(A.isdigit())  # Output: False
print(A.isalnum())  # Output: True
print(A.isspace())  # Output: False
