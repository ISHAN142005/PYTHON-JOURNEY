class Employee:
    def __init__(self, name, salary):
        # Constructor: initializes the object with name and salary
        self.name = name
        self.salary = salary

    @property
    def first_name(self):
        # Getter: when you access e.first_name, this runs
        # It splits the full name by space and returns the first part
        l = self.name.split(" ")
        return l[0]

    @first_name.setter
    def first_name(self, first):
        # Setter: when you assign e.first_name = "John", this runs
        # It replaces the first part of the name with the new one
        l = self.name.split(" ")
        new_name = f"{first} {l[1]}"
        self.name = new_name


# Create an Employee object
e = Employee("Jack Doe", 34555)

# Accessing the property calls the getter
print(e.first_name)  # Output: Jack

# Assigning to the property calls the setter
e.first_name = "John"

# Now the name has been updated
print(e.name)  # Output: John Doe
