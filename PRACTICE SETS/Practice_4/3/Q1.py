# Write a lambda function that gives square of given number and test it.

square = lambda x: x * x

num = int(input("Enter the number here:"))
print("The square of", num, "is:", square(num))

# Write a lambda function that adds two numbers and test it.

add = lambda x, y: x + y

num1 = int(input("Enter the first number here:"))
num2 = int(input("Enter the second number here:"))
print("The sum of", num1, num2, "is:", add(num1, num2))
