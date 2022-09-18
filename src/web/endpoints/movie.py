from fastapi import APIRouter, Depends, HTTPException, Query,  File, Form, UploadFile

from src.domain.movie import MovieRequest, MovieResponse
from src.usecase.save_movie_usecase import save_movie_use_case
from src.usecase.save_file_usecase import save_file_use_case

router = APIRouter()


@router.get("/{movie_id}", response_model=MovieResponse)
async def get_movie_by_id(movie_id: str):
    print("Get Movie by Id")
    return {"message": f"Hello {movie_id}"}


@router.post("/", response_model=MovieResponse)
async def save_movie(file: bytes = File(), name: str = Form(), description: str = Form(),
                     genre: str = Form(), synopsis: str = Form(), user_id: str = Form(),):
# async def save_movie(file: UploadFile):
# async def save_movie(file: bytes = File(), movie: MovieRequest = Form()):
    print("Saving Movie")
    # movie = save_movie_use_case(movie, file)
    movie = save_file_use_case(file)
    # if movie:
    #     return movie

    return {"file_size": len(file)}
