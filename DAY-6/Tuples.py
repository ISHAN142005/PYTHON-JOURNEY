# Tuples are ordered but immutable collections (cannot be changed after creation).

MyTupple = (99, 88, 77, 12)
print(MyTupple[0])
print(MyTupple[0:])
print(MyTupple[::-1])

# Sinle element tuple creation
SingleTupple = (99,)  # Using comma is mandatory

# MyTupple[3]=21 -->#Will throw an error Output:'tuple objects does not support item assignment
