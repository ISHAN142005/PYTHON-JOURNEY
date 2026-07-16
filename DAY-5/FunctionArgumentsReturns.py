# Positional Arguments-->  Values are passed to a function in the exact order of parameters.


def sum(a, b):  # Here a & b are parameters
    return a + b


print(sum(3, 6))  # Here 3 & 6 are arguments

# Default arguments-->  You can assign a default value to a parameter. If the caller doesn’t provide it, the default is used.


def product(a, b, mult=1):  # mult is default here
    x = a * b * mult


print(product(2, 5))
print(product(2, 5, 9))  # We can also override the default


# Keyword Argument-->  Instead of relying on position, you can explicitly name the parameters while calling the function.
def intro(name, age):
    print(f"Name:{name},Age:{age}")


intro(
    age=20, name="Ishan Bohra"
)  # age=20,name="Ishan Bohra"--> This are keyword arguments
