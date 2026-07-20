marks = {"Harry": 34, "Sam": 45, "Ishan": 98}  # Harry Sam Ishan -->Keys
# 34 45 98  -->Values
# We can have list as keys
# Only hashable type can be keys
print(marks.keys())
print(marks.values())
marks.pop("Sam")  # -->Removes  specified key and value
print(marks)

marks.clear()
print(marks)

# There are many more methods which we can explore
