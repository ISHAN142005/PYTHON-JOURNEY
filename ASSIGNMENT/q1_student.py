class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def calculate_total(self):
        return sum(self.marks)

    def calculate_average(self):
        return self.calculate_total() / len(self.marks)

    def display_result(self):
        print(f"Name: {self.name}")
        print(f"Total: {self.calculate_total()}")
        print(f"Average: {self.calculate_average():.2f}")


student1 = Student("Priya", 101, [80, 75, 90])
student1.display_result()
