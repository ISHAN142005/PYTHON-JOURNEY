class Employee:
    company = "HP"  # Class variable shared by all employees

    def __init__(self, name, salary):
        # Constructor: runs when you create a new Employee
        self.name = name
        self.salary = salary

    def __str__(self):
        # Called when you use str(e) or print(e)
        # Should return a nice, human-readable string
        return f"The name is {self.name} and the salary is {self.salary}"

    def __repr__(self):
        # Called when you use repr(e) or just type e in the console
        # Should return a developer-friendly representation
        return f"name: {self.name}\nsalary: {self.salary}"

    def __len__(self):
        # Called when you use len(e)
        # Here, we define length as the number of characters in the name
        return len(self.name)


# Create an Employee object
e = Employee("Harry", 43566)

# __len__ is triggered → counts characters in "Harry" (5)
print(len(e))

# Access instance variables directly
print(e.name, e.salary)

# __str__ is triggered → nice readable string
print(str(e))

# __repr__ is triggered → developer-style representation
print(repr(e))
