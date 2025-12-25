import uvicorn
import data_interactor as data_i
from fastapi import FastAPI
from database import SqlService
import mysql


app = FastAPI()


def get_cursor():
    db_connector = SqlService().connect_db()
    cursor = db_connector.cursor()
    return cursor, db_connector


@app.get('/')
def home():
    cursor, connector = get_cursor()
    if isinstance(cursor, Exception):
        return {'message' : f'failed to connect to database., {cursor}'}
    
    cursor.close()
    connector.close()
    return {'message' : 'Hello From inside the container!!'}



@app.get('/contacts')
def get_all_contacts():
    cursor, connector = get_cursor()
    contacts = data_i.get_all_contacts(cursor)
    cursor.close()
    connector.close()
    return {'All contacts' : contacts}


@app.post('/contacts')
def create_contact(contact : data_i.Contact):
    cursor, connector = get_cursor()
    new_id = data_i.create_new_contact(contact, cursor)
    connector.commit()
    cursor.close()
    connector.close()
    return {'message' : 'contact created successfully', 'new_id' : new_id}


@app.put('/contacts/{c_id}')
def update_contact(c_id, contact : data_i.Contact):
    cursor, connector = get_cursor()
    is_updated = data_i.update_contact(c_id, contact, cursor)
    connector.commit()
    cursor.close()
    connector.close()
    return {'message' : is_updated}


@app.delete('/contacts/{id}')
def delete_contact(c_id):
    cursor, connector = get_cursor()
    is_deleted = data_i.delete_contact(c_id, cursor)
    connector.commit()
    cursor.close()
    connector.close()
    return {'message' : is_deleted}


if __name__ == "__main__":
    uvicorn.run(app, port=8000, host='0.0.0.0')