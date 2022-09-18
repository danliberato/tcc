from fastapi import FastAPI, APIRouter
from dotenv import load_dotenv

from src.web.api import api_router

load_dotenv()

root_router = APIRouter()
app = FastAPI(title="UNIP 2022 - TCC")

app.include_router(api_router)
app.include_router(root_router)
