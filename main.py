import threading
import time
import operator
from concurrent.futures import thread

from license_plate_publisher import *
from notification_publisher import *
from payloads import *
import _thread
import json

wanted=[]

with open("wanted.txt", 'r') as f:
    wanted = json.loads(f.read())

updated=False # Updated

class Thread_notification(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):

        print("notification_publisher", flush=True)
        global updated

        while True:
            print("redo loop", flush=True)
            msg = notification_publisher()

            if msg is not None:
                updated = True


if __name__ == '__main__':
    print("Entered main")
    tread_publisher = Thread_notification("Publisher notifier")

    print("Starting notification thread")
    tread_publisher.start()
    print("Started notification thread")

    while True:

        if updated:

            print("UPDATED")

            updated = False
            wanted = getPayload()

            with open("wanted.txt", 'w') as f:
                f.write(json.dumps(wanted))

        payload = get_plate_information(license_plate_publisher())

        print(payload)

        if (payload["LicensePlate"] in wanted):
            sendPayload(payload)