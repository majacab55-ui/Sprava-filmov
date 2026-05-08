import json
import os
from movie import Movie

class MovieManager:
    def __init__(self, filename="movies.json"):
        self.filename = filename
        self.movies = []
        self.load_from_json()

    def add_movie(self, movie: Movie) -> None:
        self.movies.append(movie)
        self.save_to_json()

    def find_movie(self, search: str) -> Movie | None:
        for movie in self.movies:
            if search.lower() in movie.name.lower():
                return movie
        return None

    def show_movies(self) -> None:
        if not self.movies:
            print("Zoznam filmov je prázdny.")
            return
        for movie in self.movies:
            print(movie)

    def filter_by_year(self, year: int) -> list:
        """Vráti zoznam filmov zadaného roku."""
        return [movie for movie in self.movies if movie.year == year]

    def filter_by_genre(self, genre: str) -> list:
        """Vráti zoznam filmov, ktorých žáner obsahuje zadaný reťazec."""
        return [movie for movie in self.movies if genre.lower() in movie.genre.lower()]

    def filter_by_rating(self, min_rating: float = 0.0, max_rating: float = 10.0) -> list:
        """Vráti zoznam filmov v rozmedzí hodnotení."""
        return [movie for movie in self.movies if min_rating <= movie.rating <= max_rating]

    def filter_by_year_range(self, start_year: int, end_year: int) -> list:
        """Vráti zoznam filmov v rozmedzí rokov."""
        return [movie for movie in self.movies if start_year <= movie.year <= end_year]

    def save_to_json(self) -> None:
        data = []
        for movie in self.movies:
            data.append({
                "name": movie.name,
                "genre": movie.genre,
                "year": movie.year,
                "rating": movie.rating
            })
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def load_from_json(self) -> None:
        if not os.path.exists(self.filename):
            return
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return
        self.movies = []
        for item in data:
            try:
                movie = Movie(item["name"], item["genre"], item["year"], item["rating"])
                self.movies.append(movie)
            except ValueError:
                continue

    def delete_movie(self, search: str) -> bool:
        original_length = len(self.movies)
        self.movies = [
            movie for movie in self.movies
            if search.lower() not in movie.name.lower()
        ]

        if len(self.movies) < original_length:
            self.save_to_json()
            return True
        return False