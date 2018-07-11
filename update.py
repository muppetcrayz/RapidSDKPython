import app
import requests
import warnings
import sys
import json

session_id = sys.argv[1]
json_data = sys.argv[2]

warnings.filterwarnings("ignore")

url = 'http://testapi.rapidsdk.com/v1/data/update'

data = {'session_id': session_id, 'data': json.loads(json_data)}

headers = {'content-type': 'application/json'}

apiKey = app.apiKey
apiSecret = app.apiSecret

r = requests.post(url = url, data = json.dumps(data), auth=(apiKey, apiSecret), headers=headers)

print(r.text)
