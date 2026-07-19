"""
Tuples in Python are immutable, so they have only two built‑in methods: count() and index().
Other operations like len(), min(), max(), sum(), and sorted() are available as built‑in functions,
not methods.
"""

numbers = (10, 20, 30, 20, 40, 80, 20, 30)

# count(x) → returns how many times x appears in the tuple
print(numbers.count(20))  # 3

# index(x) → returns the index of the first occurrence of x
print(numbers.index(30))  # 2


'''
Why Use Tuples?
1.Faster than lists (since they are immutable)
2.Used as dictionary keys (since they are hashable)
3.Safe from unintended modifications
'''