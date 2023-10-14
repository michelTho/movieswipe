import random
import requests

from typing import Dict

from .tmdb_parser import is_tmdb_json_movie_adult, parse_tmdb_json_movie


TMDB_ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0M2U2NGRmOTVhNDMxODQxZWYzNGE4ZWVjMmVmYTVhYyIsInN1YiI6IjY1MGY0YWU5M2E0YTEyMDExY2YyZTZhNCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.pls6o4Vl0QRFoxOQjC2heqAF0DBxikpSAJfgsuKplqM"
TMDB_BASE_URL = "https://api.themoviedb.org/3/"

TMDB_LATEST_MOVIE_ROUTE = "movie/latest"
TMDB_DETAILS_MOVIE_ROUTE = "movie/"
TMDB_DETAILS_MOVIE_QUERY_PARAMS = "?language=fr-FR"


def get_random_tmdb_movie() -> Dict:
    """
    Returns a random movie from the TMDB API, by searching for a random movie below the latest movie's id.
    Note: Since not all ids are used, we search recursively until we find a movie.
    """
    latest_movie = _get_latest_tmdb_movie()
    latest_tmdb_id = latest_movie.get("tmdb_id")
    return _get_random_tmdb_movie_below_id(latest_tmdb_id)


def _get_tmdb_headers() -> Dict:
    return {
        "accept": "application/json",
        "Authorization": f"Bearer {TMDB_ACCESS_TOKEN}",
    }


def _get_latest_tmdb_movie() -> Dict:
    """
    Returns the latest movie from the TMDB API.
    """
    latest_movie_response = requests.get(
        TMDB_BASE_URL + TMDB_LATEST_MOVIE_ROUTE, headers=_get_tmdb_headers(), timeout=5
    )
    json_movie = latest_movie_response.json()
    return _get_tmdb_movie_details(json_movie["id"])


def _get_random_tmdb_movie_below_id(latest_tmdb_id: int) -> Dict:
    random_tmdb_id = random.randint(1, latest_tmdb_id)
    print(f"getting random tmdb movie with tmdb id {random_tmdb_id}")
    try:
        movie = _get_tmdb_movie_details(random_tmdb_id)
        if (
            movie.get("image_url") == ""
            or movie.get("adult") == True
            or movie.get("description") == ""
            or movie.get("original_language") not in ["en", "fr", "es", "it", "de"]
            or movie.get("popularity") < 1
        ):
            return _get_random_tmdb_movie_below_id(latest_tmdb_id)
        return movie
    except Exception:
        return _get_random_tmdb_movie_below_id(latest_tmdb_id)


def _get_tmdb_movie_details(tmdb_id: int) -> Dict:
    """
    Returns the details of a TMDB movie.
    """
    movie_response = requests.get(
        TMDB_BASE_URL
        + TMDB_DETAILS_MOVIE_ROUTE
        + str(tmdb_id)
        + TMDB_DETAILS_MOVIE_QUERY_PARAMS,
        headers=_get_tmdb_headers(),
    )
    if movie_response.status_code == 200:
        return parse_tmdb_json_movie(movie_response.json())
    else:
        raise Exception(f"TMDB id {tmdb_id} not found")
