class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Some generic sound...")


class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks: Woof!")


class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows: Meow!")


class Bird(Animal):
    def speak(self):
        print(f"{self.name} chirps: Tweet-tweet!")


pets = [Dog("Rover"), Cat("Fluffy"), Bird("Tweety")]

for pet in pets:
    pet.speak()
