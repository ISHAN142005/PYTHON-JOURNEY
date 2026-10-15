class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def apply_discount(self, percent):
        discount_amount = (self.price * percent) / 100
        final_price = self.price - discount_amount
        print(f"Original Price: {self.price}")
        print(f"Discount: {int(discount_amount)}")
        print(f"Final Price: {int(final_price)}")


my_mobile = Mobile("Samsung", "Galaxy A55", 40000)
my_mobile.apply_discount(10)
