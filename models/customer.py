class Customer:
    def __init__(self, firstname, surname, contact):
        self.firstname = firstname
        self.surname = surname
        self.contact = contact

    def __str__(self):
        return f"{self.firstname} {self.surname} - {self.contact}"