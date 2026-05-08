from datetime import datetime
CURRENT_YEAR = datetime.now().year
class Movie:
    def __init__(self, name, genre, year, rating):
        if not name.strip():
            raise ValueError("Neplatný názov filmu")
        if not genre.strip():
            raise ValueError("Neplatný žáner")
        if year < 1895 or year > CURRENT_YEAR:
            raise ValueError("Neplatný rok filmu")
        if rating < 0 or rating > 10:
            raise ValueError("Hodnotenie musí byť 0-10")

        self._name = name
        self._genre = genre
        self._year = year
        self._rating = rating

    @property
    def name(self):
        return self._name

    @property
    def genre(self):
        return self._genre

    @property
    def year(self):
        return self._year

    @property
    def rating(self):
        return self._rating

    def __str__(self):
        return f"{self.name} | {self.genre} | {self.year} | hodnotenie: {self.rating}"