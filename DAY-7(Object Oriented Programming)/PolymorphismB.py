class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("Hello, I am just a person.")


class Student(Person):
    def introduce(self):
        print(f"Hi, I’m {self.name}, and I study Computer Science.")


class Teacher(Person):
    def introduce(self):
        print(f"Good day, I’m {self.name}, and I teach Mathematics.")


class Doctor(Person):
    def introduce(self):
        print(f"Hello, I’m Dr. {self.name}, and I help people stay healthy.")


people = [Student("Ishan"), Teacher("Anita"), Doctor("Rahul")]

for person in people:
    person.introduce()
