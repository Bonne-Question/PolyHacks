import requests
import json
from requests.auth import HTTPBasicAuth

def sendPayload(payload):
    url="https://licenseplatevalidator.azurewebsites.net/api/lpr/platelocation"

    auth= HTTPBasicAuth('equipe37', 'JKPJUfnYfaxngMxb')

    r = requests.post(url, auth=auth, data=json.dumps(payload))

    print(r.status_code, r.reason)
    print(r.text)