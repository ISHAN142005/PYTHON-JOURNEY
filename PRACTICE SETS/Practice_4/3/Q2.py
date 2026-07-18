#Create a list [1, 2, 3, 4, 5] and use map() with a lambda function to get their squares.

numbers = [1, 2, 3, 4, 5]  # -->List
squares = list(map(lambda x: x * x, numbers))  # -->map with lambda function

print("Original numbers:", numbers)
print("Squares:", squares)
