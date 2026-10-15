class Employee:
    def __init__(self, name, basic_salary):
        self.name = name
        self.basic_salary = basic_salary


class Manager(Employee):
    def __init__(self, name, basic_salary, bonus):
        super().__init__(name, basic_salary)
        self.bonus = bonus

    def calculate_salary(self):
        return self.basic_salary + self.bonus


manager = Manager("John", 50000, 10000)
print(f"Name: {manager.name}")
print(f"Total Salary: {manager.calculate_salary()}")
