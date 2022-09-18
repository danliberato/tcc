import boto3
from uuid import uuid4

dynamodb = boto3.resource('dynamodb', region_name="us-east-1")
table = dynamodb.Table('movie')


def save_movie(movie):
    print(f"Saving movie - id {movie['id']}")
    try:
        response = table.put_item(
            Item={
                'id': movie['id'],
                'name': movie['name'],
                'description': movie['description'],
                'genre': movie['genre'],
                'synopsis': movie['synopsis'],
                'cover_url': movie['cover_url'],
                'user_id': movie['user_id']
            }
        )
        print(response)
        return True
    except Exception as e:
        print(e)
        return False


def get_movie(movie_id):
    print(f"Retrieving movie - id {movie_id}")
    try:
        response = table.get_item(
            Key={
                'id': movie_id
            }
        )
        return response['Item']
    except Exception as e:
        print(e)
        return None


def delete_movie(movie_id):
    print(f"Deleting movie - id {movie_id}")
    try:
        response = table.delete_item(
            Key={
                'id': movie_id
            }
        )
        return True
    except Exception as e:
        print(e)
        return False
