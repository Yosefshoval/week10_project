from pydantic import BaseModel
from dataclasses import dataclass

import database as db



@dataclass
class Contact(BaseModel):

    first_name : str
    last_name : str
    phone_number : str

    def __dict__(self):
        return {'first_name' : self.first_name,
                'last_name' : self.last_name,
                'phone_number' : self.phone_number
                }


def get_all_contacts(cursor):
    statement = f"""
    SELECT * FROM {db.TABLE};
    """
    cursor.execute(statement)
    result = cursor.fetchall()
    cursor.commit()
    return result


def search_contact_by_id(c_id, cursor):
    cursor.execute(f'SELECT * FROM {db.TABLE} WHERE id = {c_id};')
    is_there_id = cursor.fetchone()
    return is_there_id is not None



def create_new_contact(contact : Contact, cursor, db_connector):

    contact = contact.__dict__
    sql = f"INSERT INTO {db.TABLE} (first_name, last_name, phone_number) VALUES (%s, %s, %s);"
    val = (contact['first_name'], contact['last_name'], contact['phone_number'])
    
    cursor.execute(sql, val)

    cursor.execute('SELECT LAST_INSERT_ID();')
    contact_id = cursor.fetchone()
    return contact_id



def update_contact(contact_id, new_contact : Contact, cursor):

    if not search_contact_by_id(contact_id, cursor):
        return f'There is no contact with id {contact_id} in the database.'

    statement = (f"UPDATE {db.TABLE} "
            f"SET first_name = {new_contact.first_name}, "
            f"last_name = {new_contact.last_name}, "
            f"phone_number = {new_contact.phone_number} "
            f"WHERE id = {contact_id};")

    cursor.execute(statement)
    return f'contact with id {contact_id} updated successfully'




def delete_contact(contact_id, cursor):
    try:
        if not search_contact_by_id(contact_id, cursor):
            return f'There is no contact with id {contact_id} in the database.'
        statement = f''
        cursor.execute(statement)
        return 'contact deleted successfully'
    except Exception as err:
        return err
