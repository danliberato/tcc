from fastapi import APIRouter

from src.api.endpoints import user, movie


api_router = APIRouter()
api_router.include_router(user.router, prefix="/user", tags=["user"])
api_router.include_router(movie.router, prefix="/movie", tags=["movie"])
