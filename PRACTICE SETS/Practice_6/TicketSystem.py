class Ticket:
    def __init__(self, destination, seat):
        self.destination = destination
        self.seat = seat

    def describe(self):
        print(f"Ticket to {self.destination}, seat {self.seat}.")


class Passenger:
    def __init__(self, name):
        self.name = name

    def board(self, ticket):
        print(f"{self.name} boards the bus to {ticket.destination}, sitting at seat {ticket.seat}.")


ticket1 = Ticket("Udaipur", "12A")
ticket2 = Ticket("Jaipur", "7B")

passenger1 = Passenger("Ishan")
passenger2 = Passenger("Harry")

ticket1.describe()
ticket2.describe()

passenger1.board(ticket1)
passenger2.board(ticket2)