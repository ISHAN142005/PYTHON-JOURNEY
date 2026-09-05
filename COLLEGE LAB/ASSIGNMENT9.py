fruits = ["Kiwi", "Orange", "Pineapple", "Grapes"]
print("Original list:", fruits)

length = len(fruits)
print("\nTotal fruits:", length)

search_fruit = "Pineapple"
if search_fruit in fruits:
    print(f"{search_fruit} is in the basket.")
else:
    print(f"{search_fruit} is not in the basket.")

fruits_copy = fruits.copy()
print("\nCopied basket:", fruits_copy)
