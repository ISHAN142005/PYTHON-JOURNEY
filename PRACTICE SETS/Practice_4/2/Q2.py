"""
Write a function calculate_area(length, width=10) that returns the area of a rectangle. Test it by calling the function with:

Both length and width
Only length (use default width)

"""


def calculate_area(length, width=10):
    return length * width


print("The area of the rectangle is:", calculate_area(10, 20))
print("The area of the rectangle is:", calculate_area(10))
