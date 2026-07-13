import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch_all

patch_all()

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

def lambda_handler(event, context):

    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('Sales')

    response = table.scan(
        FilterExpression=Key('orderYear').eq(2017)
    )

    sortedList = sorted(response["Items"], key = lambda i: i['total'], reverse=True)

    body = json.dumps(sortedList[:3], cls=DecimalEncoder)

    return {
        'statusCode': 200,
        'body': body
    }
