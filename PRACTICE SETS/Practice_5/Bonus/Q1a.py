#Write a program that takes a list of numbers and removes all duplicates using a set.
# Version 2
number = list(map(int, input("Enter numbers separated by space: ").split()))

NewNumbers = []
seen = set()

for num in number:
    if num not in seen:
        NewNumbers.append(num)
        seen.add(num)

print("Original List:", number)
print("List without duplicates (order preserved):", NewNumbers)
