from datetime import datetime
from movie import Movie
from api import get_movie_from_api, MovieNotFoundError, APIConnectionError
from manager import MovieManager
from input_utils import get_text, get_int, get_float

CURRENT_YEAR = datetime.now().year


def movie_input():
    name = get_text("Zadaj názov filmu: ")
    genre = get_text("Zadaj žáner: ")
    year = get_int("Zadaj rok vydania filmu: ", min_val=1895, max_val=CURRENT_YEAR)
    rating = get_float("Zadaj hodnotenie (0-10): ", min_val=0.0, max_val=10.0)

    try:
        return Movie(name, genre, year, rating)
    except ValueError as e:
        print(e)
        return None


def show_menu():
    print("\n MOVIE MANAGER")
    print("1 - Pridať film ručne")
    print("2 - Pridať film z API")
    print("3 - Vyhľadať film")
    print("4 - Zobraziť všetky filmy")
    print("5 - Zmazať film")
    print("6 - Filtrovať filmy")
    print("7 - Koniec")


def handle_filtering(manager):
    print("\n--- FILTROVANIE FILMOV ---")
    print("a - Podľa roku")
    print("b - Podľa žánru")
    print("c - Podľa hodnotenia")
    print("d - Podľa rozmedzia rokov")

    choice = input("Vyber možnosť: ").lower()

    if choice == "a":
        year = get_int("Zadaj rok: ", min_val=1895, max_val=CURRENT_YEAR)
        results = manager.filter_by_year(year)

    elif choice == "b":
        genre = get_text("Zadaj žáner (časť názvu): ")
        results = manager.filter_by_genre(genre)

    elif choice == "c":
        min_rating = get_float("Minimálne hodnotenie (0-10): ", min_val=0.0, max_val=10.0)
        max_rating = get_float("Maximálne hodnotenie (0-10): ", min_val=0.0, max_val=10.0)
        results = manager.filter_by_rating(min_rating, max_rating)

    elif choice == "d":
        start_year = get_int("Od roku: ", min_val=1895, max_val=CURRENT_YEAR)
        end_year = get_int("Do roku: ", min_val=start_year, max_val=CURRENT_YEAR)
        results = manager.filter_by_year_range(start_year, end_year)

    else:
        print("Neplatná voľba.")
        return

    if not results:
        print("Žiadne filmy nevyhovujú zadaným kritériám.")
    else:
        print(f"\nNájdených filmov: {len(results)}")
        for movie in results:
            print(movie)


def handle_choice(choice: str, manager: MovieManager) -> bool:
    if choice == "1":
        movie = movie_input()
        if movie:
            manager.add_movie(movie)

    elif choice == "2":
        name = get_text("Zadaj názov filmu: ")
        try:
            movie = get_movie_from_api(name)
            manager.add_movie(movie)
            print("Film pridaný z API!")
        except MovieNotFoundError:
            print("Film sa v API nenašiel.")
        except APIConnectionError as e:
            print(f"Chyba API: {e}")

    elif choice == "3":
        search = get_text("Zadaj názov filmu: ")
        movie = manager.find_movie(search)

        if movie:
            print("Nájdené:")
            print(movie)
        else:
            print("Film sa nenašiel.")

    elif choice == "4":
        print("\nZoznam filmov:")
        manager.show_movies()

    elif choice == "5":
        search = get_text("Zadaj názov filmu na zmazanie: ")
        deleted = manager.delete_movie(search)

        if deleted:
            print("Film zmazaný.")
        else:
            print("Film sa nenašiel.")

    elif choice == "6":
        handle_filtering(manager)

    elif choice == "7":
        return False

    else:
        print("Neplatná voľba.")

    return True  # <-- TOTO BOLO CHÝBAJÚCE


def main():
    manager = MovieManager()

    running = True
    while running:
        show_menu()
        choice = input("Vyber možnosť: ")
        running = handle_choice(choice, manager)


if __name__ == "__main__":
    main()