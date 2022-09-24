import logging
from fastapi import APIRouter


from src.domain.alert import AlertRequest, AlertResponse
from src.usecase.create_alert_usecase import create_alert_use_case
from helper.alert_mapper import alert_base_to_response

router = APIRouter()


@router.post("/")
async def create_alert(alert_request: AlertRequest):
    print("Create Alert")
    try:
        alert = create_alert_use_case(alert_request)
    except Exception as e:
        logging.error(e)
    return alert_base_to_response(alert)
