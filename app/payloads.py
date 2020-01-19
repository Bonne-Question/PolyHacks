import requests
import json
from requests.auth import HTTPBasicAuth


auth= HTTPBasicAuth('equipe37', 'JKPJUfnYfaxngMxb')

def sendPayload(plate, context_reference_image):
    url="https://licenseplatevalidator.azurewebsites.net/api/lpr/platelocation"

    payload = {
        "LicensePlateCaptureTime": plate["LicensePlateCaptureTime"],
        "LicensePlate": plate["LicensePlate"],
        "Latitude": plate["Latitude"],
        "Longitude": plate["Longitude"],
        "ContextImageReference": context_reference_image
    }

    r = requests.post(url, auth=auth, data=json.dumps(payload))

    print(r.status_code, r.reason)
    print(r.text)

def getPayload():
    url="https://licenseplatevalidator.azurewebsites.net/api/lpr/wantedplates"

    r = requests.get(url, auth=auth)

    print(r.status_code, r.reason)

    return json.loads(r.text)