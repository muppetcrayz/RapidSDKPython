import requests
import warnings
import sys
import json

class RapidSDK:

    apiKey = "API_KEY"
    apiSecret = "API_SECRET"
    sessionID = ""

    def login(self, username, password):
        warnings.filterwarnings("ignore")
    
        url = 'https://api.rapidsdk.com/v1/login'
    
        data = {'username':username, 'password':password}
    
        r = requests.post(url = url, data = data, auth=(self.apiKey, self.apiSecret))
        loginJSON = json.loads(r.text)
    
        status = loginJSON['status']
    
        if (status == "Success"):
            self.sessionID = loginJSON['session_id']
            return "true"
        else:
            return "false"

    def register(self, firstname, lastname, username, password):
        warnings.filterwarnings("ignore")

        url = 'https://api.rapidsdk.com/v1/register'

        data = {'firstname': firstname, 'lastname': lastname, 'email': username, 'password': password}

        r = requests.post(url = url, data = data, auth=(self.apiKey, self.apiSecret))
        registerJSON = json.loads(r.text)
    
        status = registerJSON['status']
    
        if (status == "Success"):
            return "true"
        else:
            return "false"

    def create(self, json_data):
        warnings.filterwarnings("ignore")

        url = 'https://api.rapidsdk.com/v1/data/create'

        data = {'session_id': self.sessionID, 'data': json_data}

        headers = {'content-type': 'application/json'}

        r = requests.post(url = url, data = json.dumps(data), auth=(self.apiKey, self.apiSecret), headers=headers)
        createJSON = json.loads(r.text)
    
        status = createJSON['status']
    
        if (status == "Success"):
            return "true"
        else:
            return "false"

    def read(self, string_data):
        warnings.filterwarnings("ignore")

        url = 'https://api.rapidsdk.com/v1/data/read'

        string_data = string_data.split(',')

        data = {'session_id': self.sessionID, 'data': string_data}

        headers = {'content-type': 'application/json'}

        r = requests.post(url = url, data = json.dumps(data), auth=(self.apiKey, self.apiSecret), headers=headers)
        readJSON = json.loads(r.text)
        
        if readJSON.has_key('data'):
            return readJSON['data']
        else:
            return "false"

    def update(self, json_data):
        warnings.filterwarnings("ignore")

        url = 'https://api.rapidsdk.com/v1/data/update'

        data = {'session_id': self.sessionID, 'data': json_data}

        headers = {'content-type': 'application/json'}

        r = requests.post(url = url, data = json.dumps(data), auth=(self.apiKey, self.apiSecret), headers=headers)
        updateJSON = json.loads(r.text)
    
        status = updateJSON['status']
    
        if (status == "Success"):
            return "true"
        else:
            return "false"

    def delete(self, string_data):
        warnings.filterwarnings("ignore")

        url = 'https://api.rapidsdk.com/v1/data/delete'

        string_data = string_data.split(',')

        data = {'session_id': self.sessionID, 'data': string_data}

        headers = {'content-type': 'application/json'}

        r = requests.post(url = url, data = json.dumps(data), auth=(self.apiKey, self.apiSecret), headers=headers)
        deleteJSON = json.loads(r.text)        
        
        status = deleteJSON['status']

        if (status == "Success"):
            return "true"
        else:
            return "false"






