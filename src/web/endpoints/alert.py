import logging
from fastapi import APIRouter, Depends, HTTPException, Query


from src.domain.alert import AlertRequest, AlertResponse
from src.usecase.create_alert_usecase import create_alert_use_case

router = APIRouter()


@router.post("/")
async def create_alert(alert: AlertRequest):
    print("Create User")
    try:
        alert_res = create_alert_use_case(alert)
    except Exception as e:
        logging.error(e)
    return AlertResponse(alert_res)
