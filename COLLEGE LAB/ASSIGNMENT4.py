def check_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

def check_armstrong(n):
    original = n
    digits = len(str(n))
    total = 0

    while n > 0:
        digit = n % 10
        total = total + digit ** digits
        n = n

    return total == original

num = int(input("Enter a number: "))

if check_prime(num):
    print(num, "is a Prime number")
else:
    print(num, "is not a Prime number")

if check_armstrong(num):
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
