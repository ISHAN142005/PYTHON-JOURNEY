# Lists are ordered, mutable (changeable) collections of items.

# Creating a lsit
marks = [33, 99, 45, 89, 79]
mixed = [100, "Ishan", 9.53, True]


print(marks[0])
print(marks[0:])
print(mixed[1:5])
# print(marks[6]) #Error :Index out of bound

# Common List Methods:

my_list = [1, 2, 3]

my_list.append(4)  # [1, 2, 3, 4]
my_list.insert(1, 99)  # [1, 99, 2, 3, 4]
my_list.remove(2)  # [1, 99, 3, 4]
my_list.pop()  # Removes last element -> [1, 99, 3]
my_list.reverse()  # [3, 99, 1]
my_list.sort()  # [1, 3, 99]
