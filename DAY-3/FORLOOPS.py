# General Format --> for variable in range:(start range,end range+1)
#                       print(variable)

# output-
# start range
# start range+1
# start range+2
# start range+3
# end range

num = int(input("Enter the number whose table u want to get printed here:"))
print("The entered number is:", num)
print("Here's the table of", num)


for i in range(1, 11):
    print(num, "X", i, "=", num * i)
