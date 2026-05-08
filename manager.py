class MovieManager:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

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
            movie.show_info()