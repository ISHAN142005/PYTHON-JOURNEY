class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def describe(self):
        print(f"'{self.title}' by {self.author}.")


class Reader:
    def __init__(self, name):
        self.name = name

    def borrow(self, book):
        print(f"{self.name} borrows '{book.title}' by {book.author}.")


book1 = Book("1984", "George Orwell")
book2 = Book("The Alchemist", "Paulo Coelho")

reader1 = Reader("Ishan")
reader2 = Reader("Rashi")

book1.describe()
book2.describe()

reader1.borrow(book1)
reader2.borrow(book2)