# A function calling itself to solve a problem.
# Must have a base case to avoid infinite recursion.
# Used in algorithms like Fibonacci, Tree Traversals

# Factorial using recursion


def factorial(n):
    # Base case for recursion
    if n == 1:
        return 1
    return n * factorial(n - 1)


print(factorial(9))

# Fibonacci series using recursion


def fib(n):
    # Base case for recursion
    if n == 1 or n == 0:
        return n
    return fib(n - 1) + fib(n - 2)


# breaking down fibonnaci example for understanding

print(fib(6))  # -->8

fib(4) + fib(5)
fib(2) + fib(3) + fib(3) + fib(4)
fib(1) + fib(0) + fib(2) + fib(1) + fib(2) + fib(1) + fib(3) + fib(2)
1 + 0 + fib(2) + 1 + fib(2) + 1 + fib(3) + fib(2)
1 + 0 + fib(1) + fib(0) + 1 + fib(1) + fib(0) + 1 + fib(2) + fib(1) + fib(1) + fib(0)
1 + 0 + 1 + 0 + 1 + 1 + 1 + 1 + fib(1) + fib(0) + 1 + 1 + 0
1 + 0 + 1 + 0 + 1 + 1 + 1 + 1 + 1 + 0 + 1 + 1 + 0  # -->8
