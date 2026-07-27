class Dish:
    def __init__(self, name, spice_level):
        self.name = name
        self.spice_level = spice_level

    def describe(self):
        print(f"{self.name}, spice level: {self.spice_level}.")


class Guest:
    def __init__(self, name):
        self.name = name

    def order(self, dish):
        print(f"{self.name} orders {dish.name} with {dish.spice_level} spice.")


dish1 = Dish("Paneer Butter Masala", "Medium")
dish2 = Dish("Chicken Biryani", "Hot")

guest1 = Guest("Ishan")
guest2 = Guest("Harry")

dish1.describe()
dish2.describe()

guest1.order(dish1)
guest2.order(dish2)