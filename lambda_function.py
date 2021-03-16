import json

def lambda_handler(event, context):
    print(event)
    payload = json.loads(event['body'])

    first = payload['first']
    second = payload['second']
    operation = payload['operation']
    
    if operation not in ['addition', 'subtraction', 'multiplication', 'division']:
        return {
            'statusCode': 400,
            'body': json.dumps(f'Unknown operation')
        }
    if event['httpMethod'].lower() != 'post':
        return {
            'statusCode': 400,
            'body': json.dumps(f'Unexpected method')
        }
        
        
    if operation == 'addition':
        result = first + second
    
    return {
        'statusCode': 200,
        'body': json.dumps(f'{operation} result is {result}')
    }

