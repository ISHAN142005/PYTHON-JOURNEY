# Docstrings are used to document functions, classes, and modules. In Python, they are written in triple quotes. They are accessible using the __doc__ attribute. Here's an example:


def sum(a, b):
    """This will sum two numbers"""  # -->DocString
    c = a + b
    return c


print(sum.__doc__)


# Proper example of DocString


def add(a, b):
    """
    Returns the sum of two numbers.

    Parameters:
    a (int): The first number.
    b (int): The second number.

    Returns:
    int: The sum of the two numbers.
    """
    return a + b


print(add(2, 7))
print(add.__doc__)
