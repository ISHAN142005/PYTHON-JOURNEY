# Create a set my_set = {1, 2, 3, 3, 4} and print it. (What happens to duplicate 3?)

my_set = {1, 2, 3, 3, 4}
print(my_set)
# as we print only one 3 appears as in set duplicates not allowded

# Add 5 to the set, remove 2, and check if 4 is in the set.
my_set.add(5)
print(my_set)
my_set.remove(2)
print(my_set)


# No inbuilt method to check no present or not so we use this method
check = {4}
print(check.issubset(my_set))
