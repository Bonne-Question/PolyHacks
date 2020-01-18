from license_plate_publisher import *
from sendPayload import *


if __name__ == '__main__':
    payload = get_plate_information(license_plate_publisher())
    plate = get_plate_information(payload)
    print(plate)
    sendPayload(plate)