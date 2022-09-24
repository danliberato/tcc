import logging

from src.repository import database_repository
from src.domain.alert import AlertBase
from helper.alert_mapper import db_alert_object_to_base
from src.exceptions.exceptions import UnableToSaveAlertError, DatabaseError


def create_alert_use_case(alert: AlertBase):
    try:
        db_result = database_repository.save_alert(alert)
        db_status = db_result['HTTPStatusCode']
        if db_status is None or db_status != 200:
            raise Exception

        return alert
    except DatabaseError as dbe:
        raise UnableToSaveAlertError


def get_alert_by_movie_use_case(movie_id):
    try:
        db_alert = database_repository.retrieve_alert_by_movie_id(movie_id)
        return db_alert_object_to_base(db_alert)

    except Exception as e:
        print(e)
        return None
