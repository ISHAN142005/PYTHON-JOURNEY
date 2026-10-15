import numpy as np

arr = np.random.randn(25)
print("Random Array:")
print(arr)

smallest = arr.min()
biggest = arr.max()

idx_small = arr.argmin()
idx_big = arr.argmax()

print("Min value:", smallest, "at index", idx_small)
print("Max value:", biggest, "at index", idx_big)
