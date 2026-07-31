class Food:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def show(self):
        print(f"{self.item}, Price: {self.price} INR")

class Customer:
    def __init__(self, name):
        self.name = name

    def order(self, food, qty):
        print(f"{self.name} orders {qty} {food.item}(s), Bill: {food.price * qty} INR")

food1 = Food("Pizza", 300)
food2 = Food("Burger", 150)

customer1 = Customer("Ishan")
customer2 = Customer("luna")

food1.show()
food2.show()

customer1.order(food1, 2)
customer2.order(food2, 3)
