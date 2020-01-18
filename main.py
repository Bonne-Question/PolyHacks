from license_plate_publisher import *
from payloads import *

wanted=[]
updated=False # Updated 

if __name__ == '__main__':
    while True:
        # TODO

        if (updated):
            updated = False
            wanted = getPayload()

        payload = get_plate_information(license_plate_publisher())

        if (payload["LicensePlate"] in wanted):
            sendPayload(payload)