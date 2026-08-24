fruits = ["Papaya","Apple", "Banana", "Cherry", "Mango"]
print("Original list of fruits:", fruits)

print("\nPrinting each fruit one by one:")
for fruit in fruits:
    print(fruit)

fruits.append("Orange")
print("\nList after adding 'Orange':", fruits)

fruits.remove("Banana")
print("List after removing 'Banana':", fruits)
