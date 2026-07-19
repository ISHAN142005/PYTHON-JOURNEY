A = {1, 2, 3, 4, 5, 6, 7}
B = {3, 4, 9, 11, 14, 12}

# Common elements in both sets
print(A.intersection(B))       # → {3, 4}

# All unique elements from both sets
print(A.union(B))              # → {1, 2, 3, 4, 5, 6, 7, 9, 11, 12, 14}

# Elements in A but not in B
print(A.difference(B))         # → {1, 2, 5, 6, 7}

# Check if A is completely inside B
print(A.issubset(B))           # → False (A has extra elements not in B)

# Check if A and B share nothing
print(A.isdisjoint(B))         # → False (they share 3 and 4)

# Check if A contains all of B
print(A.issuperset(B))         # → False (A doesn’t have 9, 11, 12, 14)

# Elements in B but not in A
print(B.difference(A))         # → {9, 11, 12, 14}

# Elements in either set but not both
print(A.symmetric_difference(B)) # → {1, 2, 5, 6, 7, 9, 11, 12, 14}

# Make a copy of A
print(A.copy())                # → {1, 2, 3, 4, 5, 6, 7}
