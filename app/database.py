import os
from dotenv import load_dotenv
import mysql.connector
from pathlib import Path



load_dotenv()

TABLE = 'contact'

DB_HOST = os.getenv('DB_HOST')
DB_PASSWORD = os.getenv('MYSQL_ROOT_PASSWORD')
DB_NAME = os.getenv('MYSQL_DATABASE')


class SqlService:
    def __init__(self):
        self.name = DB_NAME
        self.user = DB_PASSWORD
        self.password = DB_PASSWORD
        self.host = DB_HOST

    def connect_db(self):
        try:
            conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.name,
            )
            cursor = conn.cursor()
            return cursor
        except mysql.connector.Error as err:
            print(f"Error connecting to MySQL: {err}")
            return err
