# MATCH CASE STATEMENTS
# Ask the user to enter day number 1-7 and print the corresponding number of the week using match case

num = int(input("Enter the Day Number here:"))
print("Entererd number is:", num)

match (num):
    case 1:
        print("The Day is Monday!")
    case 2:
        print("The Day is Tuesday!")
    case 3:
        print("The Day is Wednesday!")
    case 4:
        print("The Day is Thursday!")
    case 5:
        print("The Day is Friday!")
    case 6:
        print("The Day is Saturday!")
    case 7:
        print("The Day is Sunday!")
    case _:
        print("Invalid Input!")
