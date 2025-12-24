import database as db
# from database import SqlService


class Contact:

    def __init__(self, first_name, last_name, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number

    def __dict__(self):
        return {'first_name' : self.first_name,
                'last_name' : self.last_name,
                'phone_number' : self.phone_number
                }




def get_all_contacts(cursor):
    statement = f"""
    SELECT * FROM {db.TABLE}
    """
    cursor.execute(statement)
    return cursor.fetchall()




def create_new_contact(contact : Contact, cursor):
    sql = f"INSERT INTO {db.TABLE} (first_name, last_name, phone_number) VALUES (%s, %s, %s)"
    val = (contact.first_name, contact.last_name, contact.phone_number)
    cursor.execute(sql, val)

    con_id = cursor.execute('SELECT LAST_INSERT_ID();')
    return {"message": "Contact created successfully",
            "id": con_id }


# Here will be code to crate new contact, and insert it into db.
# Request: {
# "first_name": "John",
# "last_name": "Doe",
# "phone_number": "050-1234567"
# }
# Response: {
# "message": "Contact created successfully",
# "id": 4
# }



# Here will be code to search contact in the db by id.


# Here will be code to update an existing contact in the db (by id).


# Here will be code to delete  an existing contact in the db (by id).

