class TiredStudent:
    def __init__(self, name):
        self.name = name
        self.__motivation = 10

    def study(self):
        print(f"{self.name} is pretending to read.")


class EnggStudent(TiredStudent):
    def study(self):
        print(f"{self.name} is copying code from StackOverflow.")


generic_guy = TiredStudent("Bob")
coder_guy = EnggStudent("Alice")

generic_guy.study()
coder_guy.study()
