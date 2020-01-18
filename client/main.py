import threading
import time
import operator
from concurrent.futures import thread

from connector import get_connection
from license_plate_publisher import *
from notification_publisher import *
from payloads import *
import _thread
import json

wanted=[]

dbc = get_connection()
db_cur = dbc.cursor()


class Thread_notification(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        global wanted
        # TODO get the data from the DB and assign to wanted.
        db_cur.execute("SELECT id, plates_array FROM public.plates ORDER BY id DESC LIMIT 1;")
        wanted = json.loads(db_cur.fetchone()[1])
        print(wanted, flush=True)
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