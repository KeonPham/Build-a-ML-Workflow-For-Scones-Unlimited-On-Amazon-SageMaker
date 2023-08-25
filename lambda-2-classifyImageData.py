import json
import base64
import boto3

ENDPOINT = "image-classification-2023-08-05-15-29-18-332"
runtime= boto3.client('sagemaker-runtime')

def lambda_handler(event, context):
    # json.loads(json.dumps(event))
    # print(type(event))
    # print(event['iamge_data'])
    image = base64.b64decode(event['body']['image_data'])
    response = runtime.invoke_endpoint(EndpointName=ENDPOINT, ContentType='application/x-image', Body=image)
    inferences = response['Body'].read().decode('utf-8')
    event["inferences"] = [float(x) for x in inferences[1:-1].split(',')] 
    return {
        'statusCode': 200,
        'body': {
            "inferences": event['inferences']
        }
    }