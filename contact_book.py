from hash_table import HashTable, Node

class Contact: 
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone_number}, Email: {self.email}"

class HashTable:
    def add_contact(self, name, phone_number, email):
        contact = Contact(name, phone_number, email) # Create contact instance
        hash_index = self.hash_function(name) # Get hash index with name as key
        if not self.buckets[hash_index]: # if there is no bucket at that index/buckets = [None]
            self.buckets[hash_index] = [] # initalize it with an empty list
            self.buckets[hash_index].append(contact) # add contact to the list 
        else: # appending and collision handling
            if self.buckets[hash_index.key == name]:
                print("Contact already exists.")
                return
            else:
                self.buckets[hash_index].append(contact) 
                # append contact name to the existing linked list at that index
    
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

def test_add_contact_no_collision():
    hashtable = HashTable(size=10) # Create an empty hash table of size 10
    hashtable.add_contact("Alice", "555-432-1234", "alice@example.com") # Add contact
    index = hashtable.hash_function("Alice") # Get hash index for "Alice"
    bucket = hashtable.buckets[index] # Retrieve the bucket at that index
    assert bucket is not None # Ensure bucket is not None
    assert any(contact.name == "Alice" for contact in bucket) # verify solely "Alice" is in the bucket

def test_add_contact_with_collision():
    hashtable = HashTable(size=1) # Create a hash table of size 1 to force collision
    hashtable.add_contact("Bob", "555-111-2222", "bob@example.com") # Add first contact
    hashtable.add_contact("Charlie", "555-333-4444", "charlie@example.com") # Add second contact which will collide
    bucket = hashtable.buckets[0] # Retrieve the only bucket
    assert bucket is not None # Ensure bucket is not None
    assert any(contact.name == "Bob" for contact in bucket) # verify "Bob"
    assert any(contact.name == "Charlie" for contact in bucket) # verify "Charlie"

def test_add_duplicate_contact():
    hashtable = HashTable(size=10) # Create an empty hash table of size 10
    hashtable.add_contact("David", "555-555-5555", "david@example.com") # Add contact
    hashtable.add_contact("David", "555-555-5555", "david@example.com") # Add contact again (duplicate)
    index = hashtable.hash_function("David") # Get hash index for "David"
    bucket = hashtable.buckets[index] # Retrieve the bucket at that index
    count = sum(1 for contact in bucket if contact.name == "David") # Count occurrences of "David"
    assert count == 1 # Ensure only one instance of "David" due to previous error handling
