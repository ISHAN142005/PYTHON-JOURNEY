# The __init__ method is special. It's called the constructor. It's automatically run whenever you create a new object from a class.


class Employee:
    def __init__(self, salary, name, bond):
        self.salary = (
            salary  # Create a instance attribute of name salary & assign it with salary
        )
        self.name = name
        self.bond = bond

    def get_salary(self):
        return self.salary

    def get_info(self):
        print(
            f"The name of the employee is {self.name}.\nSalary is {self.salary}.\nBond with company is for:{self.bond} years."
        )


e1 = Employee(35000, "Samon", 2)
print(e1.get_salary())
e1.get_info()
