def arm(n, power):
    if n == 0:
        return 0
    digit = n % 10
    return digit**power + arm(n // 10, power)

num = int(input("Enter number here: "))
power = len(str(num)) 
if arm(num, power) == num:
    print("Entered number is an Armstrong Number.")
else:
    print("Entered number is not an Armstrong Number.")
