"""
Using format(), create a sentence:
"My name is John and I am 25 years old."
by passing "John" and 25 as variables.

Do the same using f-strings.
"""

sent = "My name is {} and I am {} years old."
print(sent.format("John", 25))


name = input("Enter you name here:")
age = input("Enter you age here:")

print(f"My name is {name} and I am {age} years old.")
