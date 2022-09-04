import boto3
from boto3.dynamodb.conditions import Key

TABLE_NAME = "User"

client = boto3.client('dynamodb', region_name="us-east-1")

print()
