from uuid import uuid4

from src.repository import bucket_repository, database_repository
from src.domain.movie import MovieBase, MovieResponse


def save_movie_use_case(movie_request: MovieBase):
    try:
        movie = movie_request
        movie.id = str(uuid4())
        movie.movie_url = bucket_repository.save_image()
        db_result = database_repository.save_movie(movie)

        return MovieResponse(movie)

    except Exception as e:
        print(e)
        return None


