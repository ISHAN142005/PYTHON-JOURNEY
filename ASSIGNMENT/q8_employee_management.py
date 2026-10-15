class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def calculate_bonus(self):
        pass


class Manager(Employee):
    def calculate_bonus(self):
        return int(self.get_salary() * 0.20)


class Developer(Employee):
    def calculate_bonus(self):
        return int(self.get_salary() * 0.10)


def display_details(employee):
    print(employee.name)
    print(f"Salary: {employee.get_salary()}")
    print(f"Bonus: {employee.calculate_bonus()}\n")


alice = Manager("Alice", 80000)
bob = Developer("Bob", 60000)

display_details(alice)
display_details(bob)
