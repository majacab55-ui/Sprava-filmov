class Movie:
    def movie_input(self):
        self.name = input("Zadaj meno filmu: ")
        self.genre = input("Zadaj žáner: ")
        self.year = int(input("Zadaj rok: "))
        self.rating = int(input("Zadaj hodnotenie: "))

    def show_info(self):
        print(self.name, self.genre, self.year, self.rating)

movies = []

while True:
    stop = input("Napíš 'stop' ak chceš skončiť, inak ENTER: ")

    if stop == "stop":
        break

    movie = Movie()
    movie.Movie_input()
    movies.append(movie)

print("\nZoznam filmov:")
for m in movies:
    m.show_info()