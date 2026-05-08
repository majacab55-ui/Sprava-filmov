import os
from dotenv import load_dotenv
import requests
from movie import Movie

load_dotenv()

class MovieNotFoundError(Exception):
    pass

class APIConnectionError(Exception):
    pass

def get_movie_from_api(name: str) -> Movie:
    api_key = os.getenv("OMDB_API_KEY")
    if not api_key:
        raise APIConnectionError("API kľúč nie je nastavený v .env (OMDB_API_KEY).")
    url = f"https://www.omdbapi.com/?t={name}&apikey={api_key}"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise APIConnectionError(f"Chyba pripojenia k API: {e}")

    data = response.json()

    if data.get("Response") != "True":
        raise MovieNotFoundError(f"Film '{name}' sa v API nenašiel.")

    year_str = data.get("Year")
    if year_str and year_str[:4].isdigit():
        year = int(year_str[:4])
    else:
        year = 0

    rating_str = data.get("imdbRating", "N/A")
    try:
        rating = float(rating_str) if rating_str != "N/A" else 0.0
    except ValueError:
        rating = 0.0

    return Movie(
        name=data.get("Title", name),
        genre=data.get("Genre", "Unknown"),
        year=year,
        rating=rating
    )