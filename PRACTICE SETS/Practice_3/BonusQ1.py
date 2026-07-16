# print(chr(65:91)) -->This is wrong bcoz chr only takes single

for i in range(65, 91):
    A = print(chr(i), end=" ")

print("\n")

# Write a program that counts how many vowels are in a given string.
Word = input("Enter the word/sentence here:")
sum = 0
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
for char in Word:
    if char in vowels:
        sum += 1


print(f"Number of vowels in entered word are:{sum}")


# ALTERNATE METHOD
Word = input("Enter the word/sentence here:")
vowels = "aeiouAEIOU"
count = sum(1 for char in Word if char in vowels)

print(f"Number of vowels in entered word are: {count}")
