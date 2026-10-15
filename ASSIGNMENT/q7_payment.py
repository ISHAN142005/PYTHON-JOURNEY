class Payment:
    def pay(self, amount):
        pass


class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")


class UPIPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using UPI")


class CashPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Cash")


payment1 = UPIPayment()
payment1.pay(2500)
