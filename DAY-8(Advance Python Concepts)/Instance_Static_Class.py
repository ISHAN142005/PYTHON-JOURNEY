class Employee:
    # Class variable (shared by all objects of Employee)
    company = "Samsung"

    def __init__(self, name, salary):
        # Instance variables (unique to each object)
        self.name = name
        self.salary = salary

    # Instance Method (default type of method)
    def print_info(self):
        # Works with data of a specific object (self)
        info = f"My name is {self.name} \nMy salary is {self.salary}"
        print(info)

    # Static Method (does not depend on object or class data)
    @staticmethod
    def sum(a, b):
        # Just a utility function — no 'self' or 'cls'
        return a + b

    # Class Method (works with class-level data)
    @classmethod
    def print_company(cls):
        # 'cls' refers to the class itself
        print(cls.company)

    @classmethod
    def change_company(cls, new_company):
        # Changes the class variable for ALL objects
        cls.company = new_company


# Create two Employee objects
e1 = Employee("Satish", 40000)
e2 = Employee("Harish", 45000)

# Accessing class variable directly from class
print(Employee.company)  # Samsung

# print(Employee.name) → ERROR because 'name' is an instance variable

# Instance methods work on individual objects
e1.print_info()  # Satish’s info
e2.print_info()  # Harish’s info

# Static method can be called from object or class
print(e1.sum(99, 1))  # 100

# Class method works with class-level data
e1.print_company()  # Samsung
e1.change_company("HP")  # Changes company for ALL employees
e1.print_company()  # HP
print(Employee.company)  # HP
