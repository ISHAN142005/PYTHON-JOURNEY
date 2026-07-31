class Room:
    def __init__(self, number, rate):
        self.number = number
        self.rate = rate

    def info(self):
        print(f"Room {self.number}, Rate: {self.rate} INR per night")


class Guest:
    def __init__(self, name):
        self.name = name

    def book(self, room, nights):
        print(
            f"{self.name} books Room {room.number} for {nights} nights, Bill: {room.rate * nights} INR"
        )


room1 = Room(101, 1200)
room2 = Room(202, 1500)

guest1 = Guest("Ishan")
guest2 = Guest("Harry")

room1.info()
room2.info()

guest1.book(room1, 2)
guest2.book(room2, 3)
