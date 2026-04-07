import requests

class Movie:
    def __init__(self, name, genre, year, rating):
            self.name = name
            self.genre = genre
            self.year = year
            self.rating = rating

    def show_info(self):
        print(f"Názov: {self.name}")
        print(f"Žáner: {self.genre}")
        print(f"Rok: {self.year}")
        print(f"Hodnotenie: {self.rating}")
        print("------------------")

def movie_input():
    while True:
        name = input("Zadaj meno filmu: ")
        if name.strip() == "":
            print("Chyba! Meno nemôže byť prázdne.")
        elif name.isdigit():
            print("Chyba! Meno nemôže byť iba číslo.")
        else:
            break
    while True:
        genre = input("Zadaj žáner: ")
        if genre.strip() == "":
            print("Chyba! Žáner nemôže byť prázdny.")
        elif genre.isdigit():
            print("Chyba! Žáner nemôže byť číslo.")
        else:
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
                break
        except ValueError:
            print("Chyba! Zadaj číslo.")
    while True:
        try:
            rating = float(input("Zadaj hodnotenie (0-10): "))
            if 0 <= rating <= 10:
                break
            else:
                print("Chyba! Hodnotenie musí byť od 0 do 10.")
        except ValueError:
            print("Chyba! Zadaj číslo.")

    return Movie(name, genre, year, rating)

def get_movie_from_api(name):
    api_key = "6094012a" # osobny key
    url = f"http://www.omdbapi.com/?t={name}&apikey={api_key}"

    response = requests.get(url)
    data = response.json()

    if data["Response"] == "True":
        try:
            year = int(data["Year"][:4])
        except:
            year = 0
        try:
            rating = float(data["imdbRating"]) if data["imdbRating"] != "N/A" else 0
        except:
            rating = 0

        return Movie(data["Title"], data["Genre"], year, rating)
    else:
        return None

def find_movie(movies):
    search = input("Zadaj názov filmu: ")

    for m in movies:
        if search.lower() in m.name.lower():
            print("Nájdené:")
            m.show_info()
            return

    print("Film sa nenašiel.")


movies = []

while True:
    print("\n1 - Pridať film ručne")
    print("2 - Pridať film z API")
    print("3 - Vyhľadať film")
    print("4 - Zobraziť všetky filmy")
    print("5 - Koniec")

    choice = input("Vyber možnosť: ")

    if choice == "1":
        movie = movie_input()
        movies.append(movie)

    elif choice == "2":
        name = input("Zadaj názov filmu: ")
        movie = get_movie_from_api(name)
        if movie:
            movies.append(movie)
            print("Film pridaný z API!")
        else:
            print("Film sa nenašiel.")

    elif choice == "3":
        find_movie(movies)

    elif choice == "4":
        print("\nZoznam filmov:")
        for m in movies:
            m.show_info()

    elif choice == "5":
        break

    else:
        print("Neplatná voľba.")