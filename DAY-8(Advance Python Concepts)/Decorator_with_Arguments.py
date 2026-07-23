# repeat(n) is a decorator factory → it creates a decorator that repeats a function n times
def repeat(n):
    # This is the actual decorator that takes the function
    def decorator(func):
        # Wrapper adds the repeating behavior
        def wrapper(a):
            # Run the function 'n' times
            for i in range(n):
                func(a)

        return wrapper  # Return the modified function

    return decorator  # Return the decorator itself


# Apply the decorator: sayHello will now run 10 times
@repeat(10)
def sayHello(a):
    print(f"Hello {a}")


"""
It replaces the sayHello function with this equivalent logic:

def decorator(func):
    def wrapper(a):
        for i in range(n):   # repeat n times
            sayHello(a)      # call the original function
    return wrapper
"""

# Calling sayHello actually calls the wrapper → prints "Hello Ishan" 10 times
sayHello("Ishan")
