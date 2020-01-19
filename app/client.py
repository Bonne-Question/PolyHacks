import base64
import io
import os
import threading
import time

from PIL import Image
from connector import get_connection
from license_plate_publisher import *
from payloads import *


import shutil
import json
import uuid
import socket

from license_plate_publisher import license_plate_publisher
from payloads import sendPayload

wanted=[]

dbc = get_connection()
db_cur = dbc.cursor()


hostname = socket.gethostname()
IPAddr = "35.225.60.197"#socket.gethostbyname(hostname)


def create_uri(plate):

    blob = plate["ContextImageJpg"]

    uid = uuid.uuid1()

    file_path = "/var/www/html/" + str(uid) + ".jpg"

    uri = "http://"+IPAddr+"/" + str(uid) + ".jpg"

    image = Image.open(io.BytesIO(base64.b64decode(blob)))
    image.save(file_path)

    return uri


def clean_directory(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


class Thread_cleanImages(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        try:
            clean_directory("/var/www/html/")
            time.sleep(60)
        except Exception as e:
            print(e)
            pass


class Thread_notification(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        try:

            global wanted
            db_cur.execute("SELECT id, plates_array FROM public.plates ORDER BY id DESC LIMIT 1;")
            wanted = json.loads(db_cur.fetchone()[1])
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

    thread_cleaner = Thread_cleanImages("Image Cleaner")
    thread_cleaner.start()

    if len(wanted) == 0:
        print("Waiting to start")
        while(len(wanted) == 0):
            continue
        print("Starting")

    while True:
        try:

            payload = license_plate_publisher()

            if payload["LicensePlate"] in wanted:

                sendPayload(payload, create_uri(payload))


        except Exception as e:
            print(e)
            pass