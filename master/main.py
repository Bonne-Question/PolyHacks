import threading
import time
import operator
from concurrent.futures import thread

from license_plate_publisher import *
from notification_publisher import *
from payloads import *
import _thread
import json

import psycopg2

def get_connection():
    conn = psycopg2.connect(database="genetec",
                            user="bq",
                            password="passwordBQ567",
                            host="146.148.37.192",
                            port="5432")
    return conn


def init_database(conn):
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS plates(id int PRIMARY KEY, plates_array TEXT);")
    conn.commit()



dbc = get_connection()
init_database(dbc)
db_cur = dbc.cursor()

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

            db_cur.insert()
            db_cur.execute("INSERT INTO plates(plates_array) VALUES ("+wanted+");")
            dbc.commit()