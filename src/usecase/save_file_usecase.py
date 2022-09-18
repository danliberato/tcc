from fastapi import File

from uuid import uuid4

from src.repository import bucket_repository, database_repository
from src.domain.movie import MovieBase, MovieResponse


def save_file_use_case(file: File):
    try:
        file_id = str(uuid4())
        movie_url = bucket_repository.save_image(file, file_id)
        # db_result = database_repository.save_movie(movie)

        return MovieResponse(file_id, movie_url)

    except Exception as e:
        print(e)
        return None


