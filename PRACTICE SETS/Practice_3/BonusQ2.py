# Take a user input string and check if it is a palindrome (same forwards and backwards).
word = input("Enter your input here: ")
new = word.upper()

if new == new[::-1]:
    print("This string is a pakindrome")
else:
    print("This string is not a palindrome")
