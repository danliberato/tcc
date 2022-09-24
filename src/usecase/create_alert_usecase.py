from uuid import uuid4

from src.repository import database_repository
from src.domain.alert import AlertBase, AlertRequest


def create_alert_use_case(alert_request: AlertRequest):
    try:
        alert = AlertBase(alert_request)
        alert.id = str(uuid4())
        db_result = database_repository.save_alert(alert)

        return alert

    except Exception as e:
        print(e)
        return None


def retrieve_alert_by_user_use_case(user_id):
    pass
