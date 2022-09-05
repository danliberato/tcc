from fastapi import APIRouter, Depends, HTTPException, Query

router = APIRouter()


@router.get("/{movie_id}")
async def get_movie_by_id(movie_id: str):
    print("Get Movie by Id")
    return {"message": f"Hello {movie_id}"}


@router.post("/")
async def save_movie_image():
    print("Create Movie")
    return {"message": f"Hello "}
