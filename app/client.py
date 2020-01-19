import base64
import calendar
import os
import threading
import time
from app.connector import get_connection
from app.license_plate_publisher import *
from app.payloads import *

import json
import uuid
import socket




wanted=[]

dbc = get_connection()
db_cur = dbc.cursor()


hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

def create_uri(plate):
    blob = plate["ContextImageJpg"]
    timestamp = calendar.timegm(time.gmtime())
    uid = uuid.uuid1()

    file_path = __file__+"/images/" + uid + ".jpg"

    uri = "http://"+IPAddr+"/images/" + uid + ".jpg"

    image_file = open(file_path,"w")

    image_file.write(base64.b64decode(blob))
    image_file.close()
    return uri



class Thread_notification(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        try:

            global wanted
            db_cur.execute("SELECT id, plates_array FROM public.plates ORDER BY id DESC LIMIT 1;")
            wanted = json.loads(db_cur.fetchone()[1])
            print(wanted, flush=True)
            time.sleep(10)

        except Exception as e:
            print(e)
            pass


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
        try:

            payload = license_plate_publisher()

            print(payload)

            if payload["LicensePlate"] in wanted:

                sendPayload(payload, create_uri(payload))

        except Exception as e:
            print(e)
            pass