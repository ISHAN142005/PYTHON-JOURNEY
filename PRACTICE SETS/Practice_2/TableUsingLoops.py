#user input table

num=int(input("Enter the number here:"))
print("Entered number is:",num)

print("Table of",num,"-\n")
for i in range(1,11):
    print(num,"X",i,"=",num*i)

print("Thank You :-)")