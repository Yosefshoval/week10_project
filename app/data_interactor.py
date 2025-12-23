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
