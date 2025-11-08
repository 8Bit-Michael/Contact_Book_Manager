class Node: # Linked list node for handling collisions
    def __init__(self, contact, next_node=None):
        self.contact = contact
        self.next = next_node
    
class HashTable:
    def __init__(self, size=[]):
        self.size = size
        # initialize empty buckets and multiply based on size int
        self.buckets = [None] * size

    def hash_function(self, key):
        # the sum of the ASCII values of the characters in the key divided by the number of buckets
        # giving you a randomized index that is still within the bounds of the array
        return sum(ord(char) for char in key) % len(self.buckets)

    def search_contact(self, name):
        hash_index = self.hash_function(name) # Get hash index with name as key
        bucket = self.buckets[hash_index] # Retrieve the bucket at that index
        if bucket is not None: # If bucket is not empty
            for contact in bucket: # Iterate through contacts in the bucket
                if contact.name == name: # If contact name matches
                    return f"{contact.name} found at index {contact.index}" # Return the contact
        return None # Contact not found

    def delete_contact(self, name):
        hash_index = self.hash_function(name) # Get hash index with name as key
        bucket = self.buckets[hash_index] # Retrieve the bucket at that index
        if bucket is not None: # If bucket is not empty
            for i, contact in enumerate(bucket): # Iterate through contacts in the bucket
                if contact.name == name: # If contact name matches
                    index = bucket[i]
                    del bucket[i] # Delete the contact
                    return f"{contact.name} deleted from index {index}" # Contact deleted
        return False # Contact not found

def test_node_creation():
    contact = {"name": "Alice", "phone_number": "555-1234", "email": "alice.@example.com"} 
    # Sample contact data
    node = Node(contact) 
    # Create a node with contact data
    assert node.contact == contact
    # Verify contact data is correctly assigned
    assert node.next is None

def test_hash_intialization():
    hashtable = HashTable(size=5) # Create a hash table of size 5
    assert hashtable.size == 5 # Verify the size is set correcty

def test_hash_function_consistency(): # make the same key always hash to the same index
    hashtable = HashTable(size=10) # create new hash table
    key = "testkey" # you're just generating an index for this key, not assigning any value
    index1 = hashtable.hash_function(key) # generate index first time
    index2 = hashtable.hash_function(key) # generate index second time
    assert index1 == index2 # both indexes should be the same
    print("Index for key '{}' : {}".format(key, index 1)) # the index for key 'testkey'

def test_search_existing_contact(): 
    # you don't need to handle collisions here, so no error handling for adding head nodes is necessary
    hashtable = HashTable(size=10) # Create an empty hash table of size 10
    contact = {"name": "David", "phone_number": "555-6789", "email": "david@example.com"}
    index = hashtable.hash_function(contact["name"]) # get hash index for "David"
    hashtable.buckets[index] = [contact] # Manually add contact to the bucket
    result = hashtable.search_contact("David") # Search for the contact
    assert result == contact # Verify the contact is found
    print(result)

def test_search_nonexistent_contact():
    hashtable = HashTable(size=10) # Create an empty hash table of size 10
    result = hashtable.search_contact("Eve") # Search for a non-existent contact/key
    assert result is None # Verify the contact is not found
    print(result)

def test_delete_existing_contact():
    hashtable = HashTable(size=10) # Create an empty hash table of size 10
    contact = {"name": "Frank", "phone_number": "555-9876", "email": "frank@example.com"}
    index = hashtable.hash_function(contact["name"]) # generate hash index for "Frank"
    hashtable.buckets[index] = [contact] # manually insert contact into empty bucket
    result = hashtable.delete_contact("Frank") # Delete the contact
    assert result == f"Frank deleted from index {index}" # Verify deletion message
    assert hashtable.buckets[index] == [] # Verify the bucket is now empty
    print(result)

def test_deleted_contact_head():
    hashtable = HashTable(size=10) # Create an empty hash table of size 10
    contact1 = {"name": "Grace", "phone_number": "555-1111", "email":"grace@example.com"}
    contact2 = {"name": "Greg", "phone_number": "123-456-789", "email":"greg@example.com"}
    index1 = hashtable.hash_function(contact1["name"]) # generate hash index for "Grace" key
    index2 = hashtable.hash_function(contact2["name"]) # generate hash index for "Greg" key
    hashtable.buckets[index1] = [contact1] # manually insert contacts
    hashtable.buckets[index2] = [contact2] # into their respective buckets
    result = hashtable.delete_contact("Grace") # Delete the head contact
    assert result == f"Grace deleted from index {index}" # Verify deletion message
    print(result)

def test_deleted_contact_middle():
    hashtable = HashTable(size=10) # Create an empty hash table of size 10
    contact1 = {"name": "John", "phone_number": "555-1111", "email":"john@example.com"}
    contact2 = {"name": "David", "phone_number": "123-456-789", "email":"david@example.com"}
    contact3 = {"name": "Andrew", "phone_number": "123-456-789", "email":"andrew@example.com"}
    index1 = hashtable.hash_function(contact1["name"]) # generate hash index for "John" key
    index2 = hashtable.hash_function(contact2["name"]) # generate hash index for "David" key
    index3 = hashtable.hash_function(contact3["name"]) # generate hash index for "Andrew" key
    hashtable.buckets[index1] = [contact1] # manually insert contacts
    hashtable.buckets[index2] = [contact2] # into respective buckets
    hashtable.buckets[index3] = [contact3] 
    result = hashtable.delete_contact("David") # Delete middle contact
    assert result == f"David deleted from index {index}" # Verify deletion message
    print(result)


def test_deleted_tail():
    hashtable = HashTable(size=10) # Create an empty hash table of size 10
    contact1 = {"name": "Curtis", "phone_number": "555-1111", "email":"curtis@example.com"}
    contact2 = {"name": "Thomas", "phone_number": "123-456-789", "email":" thomas@example.com"}
    index1 = hashtable.hash_function(contact1["name"]) # generate hash index for "Curtis" key
    index2 = hashtable.hash_function(contact2["name"]) # generate hash index for "Thomas" key
    hashtable.buckets[index1] = [contact1] # manually insert contacts
    hashtable.buckets[index2] = [contact2] # into their respective buckets
    result = hashtable.delete_contact("Thomas") # Delete the tail contact
    assert result == f"Thomas deleted from index {index}" # Verify deletion message
    print(result)
