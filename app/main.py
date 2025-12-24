import pydantic
import uvicorn
import data_interactor as data_i
from fastapi import FastAPI
from database import connect_to_db




app = FastAPI()
db_connector = connect_to_db()



@app.get('/contacts')
def get_all_contacts():
    contacts = data_i.get_all_contacts(db_connector, )
    return contacts


@app.post('/contacts')
def create_contact(contact : data_i.Contact):
    contact = contact

    result = data_i.create_new_contact(contact, db_connector)

    return result


@app.put('/contacts/{id}')
def update_contact():
    pass


@app.delete('/contacts/{id}')
def delete_contact():
    pass


if __name__ == "__main__":
    uvicorn.run(app, port=8000)