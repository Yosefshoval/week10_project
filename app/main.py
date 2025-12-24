import json
import pydantic
import uvicorn
import data_interactor as data_i
from fastapi import FastAPI
from database import SqlService



app = FastAPI()
db_connector = SqlService().connect_db()


@app.get('/contacts')
def get_all_contacts():
    contacts = data_i.get_all_contacts(db_connector)
    return {'All contacts' : contacts}


@app.post('/contacts')
def create_contact(contact : data_i.Contact):
    contact = contact
    new_id = data_i.create_new_contact(contact, db_connector)
    return {'message' : 'contact created successfully', 'new_id' : new_id}


@app.put('/contacts/{c_id}')
def update_contact(c_id, contact : data_i.Contact):
    is_updated = data_i.update_contact(c_id, contact, db_connector)
    return {'message' : is_updated}


@app.delete('/contacts/{id}')
def delete_contact(c_id):
    is_deleted = data_i.delete_contact(c_id, db_connector)
    return {'message' : is_deleted}


if __name__ == "__main__":
    uvicorn.run(app, port=8000)