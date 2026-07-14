# if elif else
# in els ethe thing is if non of the condition are matched then print else statement.
name = input("ENTER YOUR NAME HERE:")
age = int(input("ENTER YOUR AGE HERE:"))
print("Hii", name)
if age > 18:
    print("You can drive geared vehcile.")
elif age == 18:
    print("Book an interview!")
elif age > 16:
    print("You can drive not geared vehcile.")
elif age == 16:
    print("Book an interview for learning license.")
else:
    print("You can't drive any vehcile!")
