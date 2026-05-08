from movie import Movie
from api import get_movie_from_api, MovieNotFoundError, APIConnectionError
from manager import MovieManager

def movie_input():
    name = input("Zadaj názov filmu: ")
    genre = input("Zadaj žáner: ")
    try:
        year = int(input("Zadaj rok vydania filmu: "))
        rating = float(input("Zadaj hodnotenie (0-10): "))
    except ValueError:
        print("Neplatný číselný vstup.")
        return None

    try:
        return Movie(name, genre, year, rating)
    except ValueError as e:
        print(e)
        return None


manager = MovieManager()

while True:
    print("1 - Pridať film ručne")
    print("2 - Pridať film z API")
    print("3 - Vyhľadať film")
    print("4 - Zobraziť všetky filmy")
    print("5 - Koniec")

    choice = input("Vyber možnosť: ")

    if choice == "1":
        movie = movie_input()
        if movie:
            manager.add_movie(movie)

    elif choice == "2":
        name = input("Zadaj názov filmu: ")
        try:
            movie = get_movie_from_api(name)
            manager.add_movie(movie)
            print("Film pridaný z API!")
        except MovieNotFoundError:
            print("Film sa v API nenašiel.")
        except APIConnectionError as e:
            print(f"Chyba API: {e}")

    elif choice == "3":
        search = input("Zadaj názov filmu: ")
        movie = manager.find_movie(search)
        if movie:
            print("Nájdené:")
            movie.show_info()
        else:
            print("Film sa nenašiel.")

    elif choice == "4":
        print("Zoznam filmov:")
        manager.show_movies()

    elif choice == "5":
        break

    else:
        print("Neplatná voľba.")