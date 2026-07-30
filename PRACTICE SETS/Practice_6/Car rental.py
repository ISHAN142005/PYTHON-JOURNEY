class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def describe(self):
        print(f"{self.brand} {self.model} ready for rental.")


class Driver:
    def __init__(self, name):
        self.name = name

    def rent(self, car):
        print(f"{self.name} rents a {car.brand} {car.model}.")


car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "City")

driver1 = Driver("Ishan")
driver2 = Driver("lovely")

car1.describe()
car2.describe()

driver1.rent(car1)
driver2.rent(car2)