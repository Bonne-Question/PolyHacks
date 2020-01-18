import psycopg2


def get_connection():
    conn = psycopg2.connect(database="genetec",
                            user="bq",
                            password="passwordBQ567",
                            host="146.148.37.192",
                            port="5432")
    return conn