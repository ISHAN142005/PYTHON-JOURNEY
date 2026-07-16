# Reverse a number using while loop

num = int(input("Enter the number here: "))
print("Entered number:", num)

revnum = 0
temp = num


while temp > 0:
    digit = temp % 10
    revnum = revnum * 10 + digit
    temp = temp // 10

print("Reversed number:", revnum)
