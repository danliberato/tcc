from pathlib import Path

from fastapi import FastAPI, APIRouter
from dotenv import load_dotenv

from api.api import api_router

load_dotenv()

root_router = APIRouter()
app = FastAPI(title="TCC")


@app.get("/", status_code=200)
async def root():
    return {"message": "Hello World"}

app.include_router(api_router)
app.include_router(root_router)