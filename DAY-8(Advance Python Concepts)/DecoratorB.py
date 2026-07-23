"""
Decorstor is a function that takes a function,it crreates a new function inside body (wrapper).
Then it return that new function.
"""


def decorator(func):
    def wrapper():
        print("I am about to execute the function..........")
        func()
        print("I have executed the function..........")

    return wrapper


def sayHello():
    print("Hello Bro!")



f = decorator(sayHello)
f()


# sayHello()

"""
f will look something like this-   f is the wrapper function as we saw in the structure of decorator
def p():
        print("I am about to execute the function..........")
        print("Hello Bro!")
        print("I have executed the function..........")

"""
