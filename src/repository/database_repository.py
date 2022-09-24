import boto3
from uuid import uuid4

dynamodb = boto3.resource('dynamodb', region_name="us-east-1")
table = dynamodb.Table('alerts')


def save_alert(alert):
    print(f"Saving alerts - id {alert['id']}")
    try:
        response = table.put_item(
            Item={
                'id': alert['id'],
                'movie_name': alert['movie_name'],
                'user_name': alert['user_name'],
                'date': alert['date'],
                'title': alert['title'],
                'category': alert['category'],
                'image_url': alert['image_url']
            }
        )
        print(response)
        return True
    except Exception as e:
        print(e)
        return False


def get_movie(alert_id):
    print(f"Retrieving alert - id {alert_id}")
    try:
        response = table.get_item(
            Key={
                'id': alert_id
            }
        )
        return response['Item']
    except Exception as e:
        print(e)
        return None


def delete_movie(alert_id):
    print(f"Deleting alert - id {alert_id}")
    try:
        response = table.delete_item(
            Key={
                'id': alert_id
            }
        )
        return True
    except Exception as e:
        print(e)
        return False
