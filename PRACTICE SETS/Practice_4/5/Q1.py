"""
Import the math module and use it to:

Find the square root of 144
Calculate sin(90°) (hint: use math.radians())
"""

import math

num = int(input("Enter the number here:"))
SqrtVal = math.sqrt((num))
print("The square root of entered number(", num, ") is:", SqrtVal)

print(
    "*****************************************************************************************"
)

print("Sin(X)")
angle = int(input("Enter the value of X(in Degree) here:"))
Value = math.sin(math.radians(angle))
print(f"The value of sin({angle}°) is:", Value)

print(
    "*****************************************************************************************"
)
