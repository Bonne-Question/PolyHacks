from license_plate_publisher import *
from payloads import *


if __name__ == '__main__':
    payload = get_plate_information(license_plate_publisher())
    sendPayload(payload)