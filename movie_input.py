class Movie:
    def movie_input(self):
        while True:
            name = input("Zadaj meno filmu: ")
            if name.strip() == "":
                print("Chyba! Meno nemôže byť prázdne.")
            elif name.isdigit():
                print("Chyba! Meno nemôže byť iba číslo.")
            else:
                self.name = name
                break
        while True:
            genre = input("Zadaj žáner: ")
            if genre.strip() == "":
                print("Chyba! Žáner nemôže byť prázdny.")
            elif genre.isdigit():
                print("Chyba! Žáner nemôže byť číslo.")
            else:
                self.genre = genre
                break
        while True:
            try:
                year = int(input("Zadaj rok vydania filmu: "))
                if year < 1895: # rok prvého filmu
                    print("Chyba! Film ešte neexistoval.")
                elif year > 2026:
                    print("Chyba! Rok nemôže byť v budúcnosti.")
                elif len(str(year)) != 4:
                    print("Chyba! Rok musí mať presne 4 číslice.")
                else:
                    self.year = year
                    break

            except ValueError:
                print("Chyba! Zadaj číslo.")
        while True:
            try:
                rating = float(input("Zadaj hodnotenie (0-10): "))
                if 0 <= rating <= 10:
                    self.rating = rating
                    break
                else:
                    print("Chyba! Hodnotenie musí byť od 0 do 10.")
            except ValueError:
                print("Chyba! Zadaj číslo.")

    def show_info(self):
        print(self.name, self.genre, self.year, self.rating)

movies = []

while True:
    stop = input("Napíš 'stop' ak chceš skončiť, inak ENTER: ")

    if stop == "stop":
        break

    movie = Movie()
    movie.movie_input()
    movies.append(movie)

print("\nZoznam filmov:")
for m in movies:
    m.show_info()