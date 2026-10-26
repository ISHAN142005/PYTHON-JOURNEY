class Person:
    def __init__(self, nickname, coffee_cups_a_day, sleep_hrs, fav_snack, brain_cells_left):
        self.nickname = nickname
        self.coffee = coffee_cups_a_day
        self.sleep = sleep_hrs
        self.snack = fav_snack
        self.sanity = brain_cells_left
        
    def show_vibe(self):
        print(f"{self.nickname} runs on {self.coffee} coffees, sleeps {self.sleep}h, eats {self.snack}, and has {self.sanity} brain cells.")

dude1 = Person("Alex", 4, 3, "Doritos", 2)
gal2 = Person("Sam", 1, 8, "Apples", 100)
bro3 = Person("Jake", 6, 2, "Pizza", -1)
friend4 = Person("Mia", 2, 7, "Pasta", 50)
mate5 = Person("Leo", 0, 9, "Salad", 200)

for p in [dude1, gal2, bro3, friend4, mate5]:
    p.show_vibe()