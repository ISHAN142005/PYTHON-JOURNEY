class Pizza:
    def __init__(self, size, topping):
        self.size = size
        self.topping = topping

    def describe(self):
        print(f"A {self.size} pizza with {self.topping}.")


class Customer:
    def __init__(self, name):
        self.name = name

    def order(self, pizza):
        print(f"{self.name} orders: {pizza.size} pizza with {pizza.topping}.")


pizza1 = Pizza("Large", "Cheese")
pizza2 = Pizza("Medium", "Pepperoni")

customer1 = Customer("Ishan")
customer2 = Customer("Samita")

customer1.order(pizza1)
customer2.order(pizza2)
