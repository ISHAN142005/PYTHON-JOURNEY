# Create a small module myutils.py with a function iseven(n) that returns True if n is even. Import and use it in another Python file.


import myutils

num = int(input("Enter the number you want to check:"))
print(myutils.iseven(num))
