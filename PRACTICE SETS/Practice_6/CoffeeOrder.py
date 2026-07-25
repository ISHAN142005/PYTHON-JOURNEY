class Coffee:
    def __init__(self, size, type, extras=None):
        self.size = size
        self.type = type
        self.extras = extras if extras else "no extras"

    def describe(self):
        print(f"A {self.size} {self.type} with {self.extras}.")


class Customer:
    def __init__(self, name):
        self.name = name

    def order(self, coffee):
        print(f"{self.name} orders: {coffee.size} {coffee.type} with {coffee.extras}.")


coffee1 = Coffee("Large", "Latte", "extra shot of espresso")
coffee2 = Coffee("Medium", "Cappuccino", "almond milk")

customer1 = Customer("Ishan")
customer2 = Customer("Samita")

coffee1.describe()
coffee2.describe()

customer1.order(coffee1)
customer2.order(coffee2)