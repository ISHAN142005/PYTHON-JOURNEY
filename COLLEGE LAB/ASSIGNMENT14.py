import numpy as np

random_chaos = np.random.randn(25)
print("Tiny boi:", random_chaos.min(), "at spot:", random_chaos.argmin())
print("Big boi:", random_chaos.max(), "at spot:", random_chaos.argmax())

flat_stuff = np.arange(12)
reshaped_grid = flat_stuff.reshape(3, 4)
print("\nReshaped stuff:\n", reshaped_grid)

flat_stuff.resize(2, 6)
print("\nResized stuff directly:\n", flat_stuff)

even_spacing = np.linspace(0, 100, 5)
staring_eye = np.eye(4)
ones_block = np.ones((3, 3))