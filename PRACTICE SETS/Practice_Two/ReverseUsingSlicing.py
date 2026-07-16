# Reverse a number using slicing

num = int(input("Enter the number here: "))
print("Entered number:", num)

# Convert number to string, slice it backwards, then convert back to int
revnum = int(str(num)[::-1])

print("Reversed number:", revnum)
