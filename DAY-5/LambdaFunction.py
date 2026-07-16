# Lambda function are anonymous and inline functions
"""
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16]
"""

square = lambda x: x * x
sum = lambda x, y: x + y
sub = lambda x, y: x - y
product = lambda x, y: x * y
division = lambda x, y: x / y
remainder = lambda x, y: x % y

print(square(9))
print(sum(9, 5))
print(sub(9, 5))
print(product(9, 5))
print(division(9, 5))
print(remainder(9, 5))
