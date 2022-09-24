from fastapi import APIRouter

from src.web.endpoints import alert, movie


api_router = APIRouter()
api_router.include_router(alert.router, prefix="/alert", tags=["alert"])
api_router.include_router(movie.router, prefix="/movie", tags=["movie"])

