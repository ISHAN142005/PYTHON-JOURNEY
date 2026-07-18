# Fibonacci Sum


def sumfibonacci(n):
    if n == 0 or n == 1:
        return n

    return sumfibonacci(n - 1) + sumfibonacci(n - 2)


print(sumfibonacci(9))

"""
Write a recursive function fibonacci(n) that prints the first n Fibonacci numbers
"""


def fibonacci(n):
    """
    Print the first n Fibonacci numbers using recursion.
    """

    def fib(k):
        if k <= 1:
            return k
        return fib(k - 1) + fib(k - 2)

    for i in range(n):
        print(fib(i), end=" ")


# Example usage
fibonacci(10)  # Prints: 0 1 1 2 3 5 8 13 21 34


"""
Tree example for 4
fib(4)
 ├── fib(3)
 │    ├── fib(2)
 │    │    ├── fib(1) → 1
 │    │    └── fib(0) → 0
 │    │        (fib(2) = 1 + 0 = 1)
 │    └── fib(1) → 1
 │         (fib(3) = 1 + 1 = 2)
 └── fib(2)
      ├── fib(1) → 1
      └── fib(0) → 0
           (fib(2) = 1 + 0 = 1)

Final result: fib(4) = fib(3) + fib(2) = 2 + 1 = 3

"""
