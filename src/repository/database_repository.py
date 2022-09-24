import boto3
import logging

from src.exceptions.exceptions import DatabaseError

dynamodb = boto3.resource('dynamodb', region_name="us-east-1")
table = dynamodb.Table('alerts')


def save_alert(alert):
    print(f"Saving alerts - movie_id {alert.movie_id}")
    try:
        response = table.put_item(
            Item=alert.dict()
        )
        logging.info(f'Database response: {response}')
        return response
    except Exception as e:
        logging.error(e)
        raise DatabaseError


def retrieve_alert_by_movie_id(movie_id):
    print(f"Retrieving alert - movie_id {movie_id}")
    try:
        response = table.get_item(
            Key={
                'movie_id': movie_id
            }
        )
        logging.info(f'Database response: {response}')
        return response['Item']
    except Exception as e:
        logging.error(e)
        raise DatabaseError


def delete_alert(alert_id):
    print(f"Deleting alert - id {alert_id}")
    try:
        response = table.delete_item(
            Key={
                'id': alert_id
            }
        )
        logging.info(f'Database response: {response}')
        return True
    except Exception as e:
        logging.error(e)
        raise DatabaseError

