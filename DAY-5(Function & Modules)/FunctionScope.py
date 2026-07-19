def sum(a, b):
    c = a + b
    # here a b c are local variable
    z = 1  # It creates a local variable callled z which is destroyed after this function returns
    return c


def greet():
    z = 32  # Local variable
    print("Hello Ishan")


z = 8  # Here z is a global variable
print(z)
print(sum(3, 9))
print(z)
