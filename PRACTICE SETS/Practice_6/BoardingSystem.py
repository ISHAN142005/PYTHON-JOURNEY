class Flight:
    def __init__(self, number, destination):
        self.number = number
        self.destination = destination

    def announce(self):
        print(f"Flight {self.number} to {self.destination} is now boarding.")


class Traveler:
    def __init__(self, name):
        self.name = name

    def board(self, flight):
        print(f"{self.name} boards Flight {flight.number} to {flight.destination}.")


flight1 = Flight("AI202", "Delhi")
flight2 = Flight("AI305", "Mumbai")

traveler1 = Traveler("Ishan")
traveler2 = Traveler("John")

flight1.announce()
flight2.announce()

traveler1.board(flight1)
traveler2.board(flight2)