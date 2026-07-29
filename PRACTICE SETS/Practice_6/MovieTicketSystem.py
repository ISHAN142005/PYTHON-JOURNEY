class Movie:
    def __init__(self, title, time):
        self.title = title
        self.time = time

    def showtime(self):
        print(f"'{self.title}' starts at {self.time}.")


class Viewer:
    def __init__(self, name):
        self.name = name

    def watch(self, movie):
        print(f"{self.name} goes to watch '{movie.title}' at {movie.time}.")


movie1 = Movie("Inception", "6:00 PM")
movie2 = Movie("Interstellar", "9:00 PM")

viewer1 = Viewer("Sanya")
viewer2 = Viewer("Ishan")

movie1.showtime()
movie2.showtime()

viewer1.watch(movie1)
viewer2.watch(movie2)