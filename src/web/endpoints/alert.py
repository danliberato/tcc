import logging
from fastapi import APIRouter


from src.domain.alert import AlertRequest, AlertResponse
from src.usecase.create_alert_usecase import create_alert_use_case, get_alert_by_movie_use_case
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


@router.get("/movie/{movie_id}")
async def retrieve_alert(movie_id):
    print("Get Alert by movie_id")
    try:
        alert = get_alert_by_movie_use_case(movie_id)
        if not alert:
            return {}
    except Exception as e:
        logging.error(e)
    return alert_base_to_response(alert)
