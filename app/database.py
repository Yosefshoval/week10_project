import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

def connect_to_db():

    conn = mysql.connector.connect(
        host=f'{os.getenv('DB_HOST')}',
        user=F'{os.getenv('DB_USER')}',
        password=f'{os.getenv('DB_PASSWORD')}',
        database=f'{os.getenv('DB_NAME')}'
    )
    cursor = conn.cursor()
    create_statement = """CREATE TABLE IF NOT EXISTS contact 
                   (id INT AUTO_INCREMENT PRIMARY KEY,
                   first_name VARCHAR(50) NOT NULL,
                   last_name VARCHAR(50) NOT NULL,
                   phone_number VARCHAR(20) NOT NULL UNIQUE
                   );"""

    cursor.execute(create_statement)

    cursor.execute("SHOW TABLES")
    return cursor
