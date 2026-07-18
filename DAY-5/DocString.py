# Docstrings are used to document functions, classes, and modules. In Python, they are written in triple quotes. They are accessible using the __doc__ attribute. Here's an example:


def sum(a, b):
    """This will sum two numbers"""  # -->DocString
    c = a + b
    return c


print(sum.__doc__)


