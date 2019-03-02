import requests
import json
from secret import api_key, base_url, model_id

def sendRequest(text):
    request = {
            'text': text,
            'entities.model': model_id,
            'features': {
                'entities': {}
                }
            }
    headers = {'Content-Type': 'application/json' }
    print('request:', request)
    response = requests.post(base_url, auth=('apikey', api_key), data=json.dumps(request), headers=headers)
    print('text:', text, '\nresponse:', response.text, '\n---')
    return response

def processResponse(response):
    def _convertEntity(entity):
        return {
                'type': entity['type'],
                'text': entity['text']
            }
    try:
        entities = response.json()['entities']
        return [_convertEntity(entity) for entity in entities]
    except (KeyError, ValueError) as e:
        print('ERROR', e)
        return []


