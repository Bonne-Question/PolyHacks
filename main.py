from license_plate_publisher import *
from payloads import *

wanted=[]

if __name__ == '__main__':
    while True:
        # TODO
        if (there is an update):
            wanted = getPayload()

        payload = get_plate_information(license_plate_publisher())

        if (payload["LicensePlate"] in wanted):
            sendPayload(payload)