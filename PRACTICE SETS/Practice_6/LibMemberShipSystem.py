class Member:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.active = True

    def info(self):
        print(f"Member: {self.name}, Age: {self.age}, Active: {self.active}")

    def deactivate(self):
        self.active = False
        print(f"{self.name}'s membership is now inactive")


class Library:
    def __init__(self, name):
        self.name = name
        self.members = []

    def register(self, member):
        self.members.append(member)
        print(f"{member.name} registered at {self.name}")

    def list_members(self):
        print(f"Members of {self.name}:")
        for m in self.members:
            print(f"- {m.name} ({'Active' if m.active else 'Inactive'})")


library = Library("City Library")

member1 = Member("Ishan", 20)
member2 = Member("Harry", 22)

library.register(member1)
library.register(member2)

member1.info()
member2.info()

member2.deactivate()

library.list_members()
