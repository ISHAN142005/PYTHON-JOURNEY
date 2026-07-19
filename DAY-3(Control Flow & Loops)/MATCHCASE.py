# SIMILAR TO THE SWITCH CASE
num = int(input("Enter a number between 1-10 here:"))
print("Your number is :", num)

# match (num):     we can use ( ) also in complex cases

match num:
    case 1:
        print("You won $10!")
    case 5:
        print("Ypu won a smartphone!")
    case 9:
        print("You won a headphone!")
    case _:
        print("Better Luck Next Time :-(")
print("See You Next time.")
