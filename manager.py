import json
import os

class MovieManager:
    def __init__(self, filename="movies.json"):
        self.filename = filename
        self.movies = []
        self.load_from_json()

    def add_movie(self, movie):
        self.movies.append(movie)
        self.save_to_json()

    def find_movie(self, search):
        for movie in self.movies:
            if search.lower() in movie.name.lower():
                return movie
        return None

    def show_movies(self):
        if not self.movies:
            print("Zoznam filmov je prázdny.")
            return
        for movie in self.movies:
            print(movie)  # použije __str__ z Movie

    def save_to_json(self):
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

    def load_from_json(self):
        if not os.path.exists(self.filename):
            return
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return
        from movie import Movie
        self.movies = []
        for item in data:
            try:
                movie = Movie(item["name"], item["genre"], item["year"], item["rating"])
                self.movies.append(movie)
            except ValueError:
                continue