from uuid import uuid4

from src.repository import database_repository
from src.domain.alert import AlertRequest
from helper.alert_mapper import alert_request_to_base


def create_alert_use_case(alert_request: AlertRequest):
    try:
        alert = alert_request_to_base(alert_request)
        db_result = database_repository.save_alert(alert)

        return alert

    except Exception as e:
        print(e)
        return None


def get_alert_by_movie_use_case(movie_id):
    try:
        return database_repository.retrieve_alert_by_movie_id(movie_id)

    except Exception as e:
        print(e)
        return None
