# Methods in Lists
# Most list methods work in-place, directly altering the list you call them on.

numbers = [1, 2, 3]

# append() → adds a single element at the end
a = numbers.append(4)
print(a)  # None (because list is modified in-place)
print(numbers)  # [1, 2, 3, 4]

# extend() → adds multiple elements from another iterable
b = numbers.extend([5, 6])
print(b)  # None
print(numbers)  # [1, 2, 3, 4, 5, 6]

# insert() → places an element at a specific index
c = numbers.insert(2, 99)
print(c)  # None
print(numbers)  # [1, 2, 99, 3, 4, 5, 6]

# remove() → deletes the first occurrence of the given value
d = numbers.remove(99)
print(d)  # None
print(numbers)  # [1, 2, 3, 4, 5, 6]

# pop() → removes and returns the last element by default
e = numbers.pop()
print(e)  # 6 (the removed element)
print(numbers)  # [1, 2, 3, 4, 5]

# sort() → arranges the list in ascending order (in-place)
f = numbers.sort()
print(f)  # None
print(numbers)  # [1, 2, 3, 4, 5]

# reverse() → flips the list order (in-place)
g = numbers.reverse()
print(g)  # None
print(numbers)  # [5, 4, 3, 2, 1]
