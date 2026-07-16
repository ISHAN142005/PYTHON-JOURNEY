"""
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!
"""

# def is used to create a function


def avg(num1, num2, num3):  # --->
    average = (num1 + num2 + num3) / 3  # --->Function Declaration
    return average  # --->


n1 = int(input("Enter the first number here:"))
n2 = int(input("Enter the second number here:"))
n3 = int(input("Enter the third number here:"))

print(
    f"The average of {n1},{n2},{n3} is:{avg(n1,n2,n3)}"
)  # avg(n1,n2,n3)-->Function call

a1 = avg(2, 3, 4)
a2 = avg(4, 7, 9)

print(
    a1
)  # we used return in our function but if we had used print d then it would give output as none
print(
    a2
)  # we used return in our function but if we had used print d then it would give output as none
