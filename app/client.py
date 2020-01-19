import base64
import calendar
import io
import os
import threading
import time

from PIL import Image
from connector import get_connection
from license_plate_publisher import *
from payloads import *

import json
import uuid
import socket

from app.license_plate_publisher import license_plate_publisher
from app.payloads import sendPayload

wanted=[]

dbc = get_connection()
db_cur = dbc.cursor()


hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

def create_uri(plate):
    blob = plate["ContextImageJpg"]

    uid = uuid.uuid1()

    file_path = "../images/" + str(uid) + ".jpg"

    uri = "http://"+IPAddr+"/images/" + str(uid) + ".jpg"

    image = Image.open(io.BytesIO(base64.b64decode(blob)))
    image.save(file_path)

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