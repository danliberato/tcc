import logging
from fastapi import APIRouter, HTTPException


from src.domain.alert import AlertRequest, AlertResponse
from src.usecase.create_alert_usecase import create_alert_use_case, get_alert_by_movie_use_case
from helper.alert_mapper import alert_base_to_response, alert_request_to_base
from src.exceptions.exceptions import UnableToSaveAlertError

router = APIRouter()


@router.post("/")
async def create_alert(alert_request: AlertRequest):
    print("Create Alert")
    try:
        alert_base = alert_request_to_base(alert_request)
        alert = create_alert_use_case(alert_base)
    except UnableToSaveAlertError:
        raise HTTPException(status_code=500, detail="Error while saving alert in database")
    except Exception as e:
        logging.error(e)
    return alert_base_to_response(alert)


@router.get("/movie/{movie_id}", response_model=AlertResponse)
async def retrieve_alert(movie_id):
    print("Get Alert by movie_id")
    try:
        alert = get_alert_by_movie_use_case(movie_id)
        if not alert:
            return {}
    except Exception as e:
        logging.error(e)
    return alert_base_to_response(alert)
