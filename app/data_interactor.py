


# Here will be code to crate database connection

class Contact:

    def __init__(self, con_id, first_name, last_name, phone_number):
        self.con_id = con_id
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number

    def convert_to_dict(self):
        return {'id' : self.con_id,
                'first_name' : self.first_name,
                'last_name' : self.last_name,
                'phone_number' : self.phone_number
                }




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

