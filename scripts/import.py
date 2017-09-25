import boto3
import json
import decimal

dynamodb = boto3.resource('dynamodb', region_name='us-west', endpoint_url="http://localhost:8000")

table = dynamodb.Table('classes')

with open("barbarian.json") as json_file:
    dnd_class = json.load(json_file)
    table.put_item(dnd_class)