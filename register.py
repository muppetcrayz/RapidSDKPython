import app
import requests
import warnings
import sys

firstname = sys.argv[1]
lastname = sys.argv[2]
username = sys.argv[3]
password = sys.argv[4]

warnings.filterwarnings("ignore")

url = 'http://testapi.rapidsdk.com/v1/register'

data = {'firstname': firstname, 'lastname': lastname, 'email': username, 'password': password}

apiKey = app.apiKey
apiSecret = app.apiSecret

r = requests.post(url = url, data = data, auth=(apiKey, apiSecret))

print(r.text)
