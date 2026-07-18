# Write a recursive function sum_of_digits(n) that returns the sum of all digits of a given number.


def sum_of_digit(n):
    if n == 0:
        return 0

    return (n % 10) + sum_of_digit(n // 10)


'''
input 1234
At last recursion return (1 % 10) + sum_of_digits(1 // 10) --> 1//10=0
                            1     +  sum_of_digits(0)
                            1     +         0 
'''

a = int(input("Enter the number here:"))
print("The sum of all the digits of enteredd number(", a, ") is:", sum_of_digit(a))
