import requests
import json
from requests.auth import HTTPBasicAuth


auth= HTTPBasicAuth('equipe37', 'JKPJUfnYfaxngMxb')

def sendPayload(payload):
    url="https://licenseplatevalidator.azurewebsites.net/api/lpr/platelocation"

    r = requests.post(url, auth=auth, data=json.dumps(payload))

    print(r.status_code, r.reason)
    print(r.text)

def getPayload():
    url="https://licenseplatevalidator.azurewebsites.net/api/lpr/wantedplates"

    #r = requests.get(url, auth=auth)

    #print(r.status_code, r.reason)

    #return json.loads(r.text)

    return json.loads('["005AFA","006ZCC","041PSJ","048MQJ746","060BJQ","072WGT","075VJN","106WER","150HZN","170YYT","490RVQ","850WPS"]')