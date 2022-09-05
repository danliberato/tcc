import boto3
from uuid import uuid4

dynamodb = boto3.client('dynamodb', region_name="us-east-1")
table = dynamodb.Table('movie')


def save_movie(movie):
    print(f"Saving movie - id {movie['id']}")
    response = table.put_item(
        Item={
            'id': {'S': uuid4()},
            'name': {'S': movie['name']},
            'description': {'S': movie['description']},
            'synopsis': {'S': movie['synopsis']},
            'cover_id': {'S': movie['cover']}
        }
    )
    print(response)


def get_movie(movie_id):
    response = table.get_item(
        Key={
            'id': movie_id
        }
    )
    item = response['Item']
    print(item)
