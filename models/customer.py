class Customer:
    def __init__(self, firstname, surname, contact=None):
        self.firstname = firstname
        self.surname = surname
        self.contact = contact

class Contact:
    def __init__(self, phone, mobile, email, address):
        self.phone = phone
        self.mobile = mobile
        self.email = email
        self.address = address