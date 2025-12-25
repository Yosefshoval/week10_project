import os
from dotenv import load_dotenv
import mysql.connector
from pathlib import Path


load_dotenv()

TABLE = 'contacts'

DB_HOST = os.getenv('DB_HOST', 'db')
DB_PASSWORD = os.getenv('MYSQL_ROOT_PASSWORD', 'root')
DB_USER = os.getenv('MYSQL_USER', 'root')
DB_NAME = os.getenv('MYSQL_DATABASE', 'contacts_db')


class SqlService:
    def __init__(self):
        self.name = DB_NAME
        self.user = DB_USER
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
            
            return conn
        except Exception as err:
            print(f"Error connecting to MySQL: {err}")
            return err
