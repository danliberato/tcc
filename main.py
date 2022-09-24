from fastapi import FastAPI, APIRouter
from dotenv import load_dotenv
from fastapi_health import health

from src.web.api import api_router


def healthy_condition():
    return {"service": "online"}


load_dotenv()

root_router = APIRouter()
app = FastAPI(title="UNIP 2022 - TCC")
app.add_api_route("/health", health([healthy_condition]), description="Healthcheck endpoint", include_in_schema=False)

app.include_router(api_router)
app.include_router(root_router)
