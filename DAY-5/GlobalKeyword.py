# To modify a global variable inside a function, use the global keyword:
def sum(a, b):
    print("Hey I am summiing!")
    c = a + b
    global z  # Please modify global z
    z = 0  # This will refer to globsl z not local varaible z
    return c


z = 3
print(sum(3, 1))
print(z)

# This allows functions to change global variables, but excessive use of global is discouraged as it can make debugging harder.
