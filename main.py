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

class Thread_notification(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        # TODO get the data from the DB and assign to wanted.

        time.sleep(10)



if __name__ == '__main__':
    print("Entered main")
    tread_publisher = Thread_notification("Publisher notifier")

    print("Starting notification thread")
    tread_publisher.start()
    print("Started notification thread")
    
    if len(wanted) == 0:
        print("Waiting to start")
        while(len(wanted) == 0):
            continue
        print("Starting")


    while True:

        payload = get_plate_information(license_plate_publisher())

        print(payload)

        if (payload["LicensePlate"] in wanted):
            sendPayload(payload)