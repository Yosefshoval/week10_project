import pydantic

from fastapi import FastAPI
from data_interactor import Contact




app = FastAPI()


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