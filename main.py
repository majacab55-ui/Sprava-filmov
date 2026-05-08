from movie import Movie
from api import get_movie_from_api, MovieNotFoundError, APIConnectionError
from manager import MovieManager
from input_utils import get_text, get_int, get_float

def movie_input():
    name = get_text("Zadaj názov filmu: ")
    genre = get_text("Zadaj žáner: ")
    year = get_int("Zadaj rok vydania filmu: ", min_val=1895, max_val=2026)
    rating = get_float("Zadaj hodnotenie (0-10): ", min_val=0.0, max_val=10.0)
    try:
        return Movie(name, genre, year, rating)
    except ValueError as e:
        print(e)
        return None

def main():
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
                print(movie)          # namiesto movie.show_info() – funguje vďaka __str__
            else:
                print("Film sa nenašiel.")

        elif choice == "4":
            print("Zoznam filmov:")
            manager.show_movies()

        elif choice == "5":
            break

        else:
            print("Neplatná voľba.")

if __name__ == "__main__":
    main()