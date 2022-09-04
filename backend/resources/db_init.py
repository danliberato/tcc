import boto3
import json

dynamodb = boto3.client('dynamodb')


with open('data.json', 'r') as datafile:
    users = json.load(datafile)
for user in users:
    print(user)
    item = {
            'name': {'S':user['name']},
            'email': {'S':user['email']},
            'id':{'S': user['id']},
            'birthdate':{'S': str(user['birthdate'])},
    }
    print(item)
    response = dynamodb.put_item(
        TableName='User',
        Item=item
    )
    print("UPLOADING ITEM")
    print(response)
