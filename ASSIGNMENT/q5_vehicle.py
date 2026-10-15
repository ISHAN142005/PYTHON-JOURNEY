class Vehicle:
    def display_type(self):
        print("This is a vehicle")


class Car(Vehicle):
    def display_type(self):
        print("This is a car")


class Bike(Vehicle):
    def display_type(self):
        print("This is a bike")


my_car = Car()
my_bike = Bike()

my_car.display_type()
my_bike.display_type()
