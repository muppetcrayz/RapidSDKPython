import app
import requests
import warnings
import sys

username = sys.argv[1]
password = sys.argv[2]

warnings.filterwarnings("ignore")

url = 'http://testapi.rapidsdk.com/v1/login'

data = {'username':username, 'password':password}

apiKey = app.apiKey
apiSecret = app.apiSecret

r = requests.post(url = url, data = data, auth=(apiKey, apiSecret))

print(r.text)
