from typing import Dict

TMDB_BASE_IMAGE_URL = "http://image.tmdb.org/t/p"
TMDB_IMAGE_SIZE = "/w500"


def is_tmdb_json_movie_adult(tmdb_json_movie: Dict) -> bool:
    """
    Checks if a TMDB JSON movie is adult or not
    """
    if "adult" not in tmdb_json_movie:
        raise AttributeError("TMDB JSON movie does not contain 'adult' key")
    if not tmdb_json_movie["adult"]:
        return False
    return True


def parse_tmdb_json_movie(tmdb_json_movie: Dict) -> Dict:
    """
    Parses a TMDB JSON movie into a Movie model, and save it to the database.
    """
    movie = {
        "title": tmdb_json_movie["title"],
        "description": tmdb_json_movie["overview"],
        "image_url": TMDB_BASE_IMAGE_URL
        + TMDB_IMAGE_SIZE
        + tmdb_json_movie["poster_path"]
        if tmdb_json_movie["poster_path"]
        else "",
        "tmdb_id": tmdb_json_movie["id"],
        "adult": tmdb_json_movie["adult"],
        "popularity": tmdb_json_movie["popularity"],
        "original_language": tmdb_json_movie["original_language"],
    }
    return movie
