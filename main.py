import threading
import time
import operator
from concurrent.futures import thread

from license_plate_publisher import *
from notification_publisher import *
from payloads import *
import _thread

wanted=[]
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
    print("creating thread")
    tread_publisher = Thread_notification("Publisher notifier")

    tread_publisher.start()

    while True:

        if updated:

            print("Updated")

            updated = False
            wanted = getPayload()

        # payload = get_plate_information(license_plate_publisher())

        # if (payload["LicensePlate"] in wanted):
            # sendPayload(payload)