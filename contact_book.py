class Contact: 
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone_number}, Email: {self.email}"

class HashTable:
    def add_contact(self, name, phone_number, email):
        pass
    
    def search_contact(self, name):
        pass

    def delete_contact(self, name)
        pass
    
    def display_all(self): 
        pass

def test_contact_creation():
    contact = Contact("John Doe", "123-456-7890", "john.doe@example.com")
    assert contact.name == "John Doe"
    assert contact.phone_number == "123-456-7890"
    assert contact.email == "john.doe@example.com"

def test_contact_display():
    contact = Contact("Jane Smith", "098-765-4321", "jane.smith@example.com")
    assert str(contact) == "Name: Jane Smith, Phone: 098-765-4321, Email: jane.smith@example.com"
    
