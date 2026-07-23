# A decorator is a function that takes another function as input
def decorator(func):
    # Define a wrapper function inside the decorator
    def wrapper():
        print("I am about to execute the function..........")
        
        # Call the original function
        func()
        
        print("I have executed the function..........")
    
    # Return the wrapper function
    return wrapper

# Apply the decorator to sayHello using @decorator
@decorator
def sayHello():
    print("Hello Bro!")

# When we call sayHello(), it actually calls the wrapper function
sayHello()
