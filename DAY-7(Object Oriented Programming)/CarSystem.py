class Car:
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        print(f"The {self.brand} car is driving.")


class Driver:
    def __init__(self, name):
        self.name = name

    def start_trip(self, car):
        print(f"{self.name} starts the trip in a {car.brand} car.")
        car.drive()


my_car = Car("Toyota")
my_driver = Driver("Ishan")

my_driver.start_trip(my_car)
