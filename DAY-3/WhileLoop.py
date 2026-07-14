"""
i=1                <--Initialisation
while i<5:         <--Condition
    print(i)       <--Printing statement
    i+=1           <--Upgradation
"""

# WAP to print the even number till the range user enters in a single line
num = int(input("Enter the end range till where you want to print even numbers:"))
print("The range given for printing even number is (0,", num, ")")

print(
    "------------------------------------------------------------------------------------------"
)


i = 1
while i < (num / 2):
    print(i * 2, end=" ")
    i += 1

print(
    "\n------------------------------------------------------------------------------------------"
)
print("Thanks:-(")
