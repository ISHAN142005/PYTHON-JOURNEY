"""
Write a function multiply(a, b) that has a proper docstring explaining what it does. Then use help(multiply) to display the docstring.
"""


def multiply(a, b):
    """
    The main moto of this function is multiplication of two numbers

    Parameters:
    This  function multiple has two parameters
    1.a-->This is a number(int or float)
    1.b-->This is an number(int or float)

    Returns:
    Product of this parameters(a*b)-->Int or Float
    """
    return a * b


print(multiply.__doc__)  # -->Calling DocString
print(multiply(3, 9))

# help(multiply) -->We can use this

"""
Comments are ignored by Python.

Docstrings are stored and can be accessed programmatically (help() or .__doc__).
"""
