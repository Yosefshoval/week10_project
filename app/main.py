import pydantic
from fastapi import FastAPI
from data_interactor import Contact
from database import connect_to_db



app = FastAPI()
db_connector = connect_to_db()



@app.get('/contacts')
def get_all_contacts():
    pass


@app.post('/contacts')
def create_contact(contact : Contact):
    pass


@app.put('/contacts/{id}')
def update_contact():
    pass


@app.delete('/contacts/{id}')
def delete_contact():
    pass