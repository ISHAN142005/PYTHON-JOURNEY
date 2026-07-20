"""
Create a dictionary of three friends and their phone numbers. Use:

keys() to get all names
values() to get all numbers
items() to loop over key-value pairs and print them
"""

MobNumbers = {"Harish": 8290912345, "Samir": 9414312345, "Shanaya": 921134567}
print(MobNumbers.keys())
print(MobNumbers.values())
print(MobNumbers.items())

for key, values in MobNumbers.items():
    print(key, values)
