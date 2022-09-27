from fastapi import FastAPI, APIRouter
from dotenv import load_dotenv
from fastapi_health import health
from fastapi_utils.tasks import repeat_every

from src.web.api import api_router
from src.usecase.send_email_usecase import send_alert_emails


def healthy_condition():
    return {"service": "online"}


load_dotenv()

root_router = APIRouter()
app = FastAPI(title="UNIP 2022 - TCC")
app.add_api_route("/health", health([healthy_condition]), description="Healthcheck endpoint", include_in_schema=False)

app.include_router(api_router)
app.include_router(root_router)


@app.on_event("startup")
@repeat_every(seconds=1)
def email_job() -> None:
    send_alert_emails()
