# Write a program that takes a list of numbers and removes all duplicates using a set.

number = list(map(int, input("Enter the number here seprated by space:").split()))

SetNumber = list(set(number))

print("Original List:", number)
print("List without duplicates:", SetNumber)


