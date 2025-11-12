from hash_table import HashTable, Node 

def test_node_creation():
    contact = {"name": "Alice", "phone_number": "555-1234", "email": "alice.@example.com"} 
    # Sample contact data
    node = Node(contact) 
    # Create a node with contact data
    assert node.contact == contact
    # Verify contact data is correctly assigned
    assert node.next is None

def test_hash_initialization():
    print('=== Hash Initialization ===')
    hashtable = HashTable(size=5) # Create a hash table of size 5
    assert hashtable.size == 5 # Verify the size is set correcty
    print('Hash table successfully initialized')

def test_hash_function_consistency(): # make the same key always hash to the same index
    print('=== Hash Consistency Test ===')
    hashtable = HashTable(size=10) # create new hash table
    key = "testkey" # you're just generating an index for this key, not assigning any value
    index1 = hashtable.hash_function(key) # generate index first time
    index2 = hashtable.hash_function(key) # generate index second time
    assert index1 == index2 # both indexes should be the same
    print("Index for key '{}' : {}".format(key, index1)) # the index for key 'testkey'

def test_search_existing_contact(): 
    print('=== Search Existent Contact Test ===')
    # you don't need to handle collisions here, so the implementation of chaining is unnecessary
    hashtable = HashTable(size=10) # Create an empty hash table of size 10
    contact = {"name": "Alice", "phone_number": "555-1234", "email": "alice.@example.com"} 
    node = Node(
        contact=contact # make it so that the list contact becomes the node's data
    )
    index = hashtable.hash_function(node.contact["name"]) # get hash index for "David"
    hashtable.buckets[index] = [node] # Manually add contact node to the bucket
    result = hashtable.search_contact("Alice") # Search for the contact
    print(result)

def test_delete_existing_contact():
    print('=== Delete Existing Contact Test ===')
    hashtable = HashTable(size=10) # Create an empty hash table of size 10
    contact = {"name": "Frank", "phone_number": "555-9876", "email": "frank@example.com"}
    index = hashtable.hash_function(contact["name"]) # generate hash index for "Frank"
    hashtable.buckets[index] = [contact] # manually insert contact into empty bucket
    result = hashtable.delete_contact("Frank") # Delete the contact
    assert result == f"Frank deleted from index {index}, position 0" # Verify deletion message with position
    assert len(hashtable.buckets[index]) == 0 # Verify the bucket is now empty
    print(result)

def test_deleted_contact_head():
    print('=== Delete Contact Head Test ===')
    hashtable = HashTable(size=10) # Create an empty hash table of size 10
    contact1 = {"name": "Grace", "phone_number": "555-1111", "email":"grace@example.com"}
    contact2 = {"name": "Greg", "phone_number": "123-456-789", "email":"greg@example.com"}
    index1 = hashtable.hash_function(contact1["name"]) # generate hash index for "Grace" key
    index2 = hashtable.hash_function(contact2["name"]) # generate hash index for "Greg" key
    hashtable.buckets[index1] = [contact1] # manually insert contacts
    hashtable.buckets[index2] = [contact2] # into their respective buckets
    result = hashtable.delete_contact("Grace") # Delete the head contact
    assert result == f"Grace deleted from index {index1}, position 0" # Verify deletion message
    print(result)

def test_deleted_contact_middle():
    print('=== Deleted Contact Middle Test ===')
    hashtable = HashTable(size=1) # Create an empty hash table of size 1, forcing collision
    contact1 = {"name": "John", "phone_number": "555-1111", "email":"john@example.com"}
    contact2 = {"name": "David", "phone_number": "123-456-789", "email":"david@example.com"}
    contact3 = {"name": "Andrew", "phone_number": "123-456-789", "email":"andrew@example.com"}
    index1 = hashtable.hash_function(contact1["name"]) # generate resued index
    hashtable.buckets[index1] = [contact1, contact2, contact3] # put all into one index
    result = hashtable.delete_contact("David") # Delete middle contact
    assert result == f"David deleted from index {index1}, position 1" # Verify deletion message with index/position
    print(result)

def test_deleted_tail():
    print('=== Deleted Contact Tail ===')
    hashtable = HashTable(size=1) # Create an empty hash table of size 10
    contact1 = {"name": "Curtis", "phone_number": "555-1111", "email":"curtis@example.com"}
    contact2 = {"name": "Thomas", "phone_number": "123-456-789", "email":" thomas@example.com"}
    index1 = hashtable.hash_function(contact1["name"]) # generate example hash key
    hashtable.buckets[index1] = [contact1, contact2] # manually insert contact into same bucket
    result = hashtable.delete_contact("Thomas") # Delete the tail contact
    assert result == f"Thomas deleted from index {index1}, position 1" # Verify deletion message with position
    print(result)

def test_display_all_contacts():
    print('=== Display Contacts Test ===')
    hashtable = HashTable(size=10) # create an empty hash table of size 10
    contact1 = {"name": "Ellen", "phone_number" : "555-2222", "email":"ellen@example.com"}
    contact2 = {"name": "Frank", "phone_number" : "555-3333", "email":"frank@example.com"}
    index1 = hashtable.hash_function(contact1["name"]) # generate hash index for "Ellen" key
    index2 = hashtable.hash_function(contact2["name"]) # generate hash index for "Frank" key
    hashtable.buckets[index1] = [contact1] # insert contact1 at that bucket
    hashtable.buckets[index2] = [contact2] # insert contact2 at that bucket
    print("Displaying all contacts for key 'Ellen':")
    print(hashtable.display_all("Ellen"))

def test_load_factor():
    print('=== Load Factor Test ===')
    hashtable = HashTable(size=10) # Create an empty hash table
    assert hashtable.get_load_factor() == 0 # Initially load factor should be 0
    contact1 = {"name" : "Gina", "phone_number" : "555-4444", "email":"gina@example.com"}
    contact2 = {"name" : "Hank", "phone_number" : "555-5555", "email":"hank@example.com"}
    index1 = hashtable.hash_function(contact1["name"]) # generate hash index for "Gina" key
    index2 = hashtable.hash_function(contact2["name"]) # generate hash index for "Hank" key
    hashtable.buckets[index1] = [contact1] # insert contact
    hashtable.buckets[index2] = [contact2] # insert contact
    result = hashtable.get_load_factor()
    assert hashtable.get_load_factor() == 0.2
    print(result)

def test_empty_table_behavior():
    print('=== Empty Table Navigation ===')
    hashtable = HashTable(size=5) # Create an empty hash table of size 5
    # Nonexistent contact search
    result = hashtable.search_contact("Alice")
    assert result == "Alice not found."
    print(result)

    print('=== Contact Deletion Test ====')
    # Nonexistent contact deletion
    result = hashtable.delete_contact("Bob")
    assert result == "Bob not found"
    print(result)

    # load nonexistent load factor
    assert hashtable.get_load_factor() == 0
    result = hashtable.get_load_factor() # Get load factor of empty table
    print(result)
    assert hashtable.get_load_factor() == 0
    result = hashtable.get_load_factor() # Get load factor of empty table
    print(result)

test_node_creation()
test_hash_initialization()
test_hash_function_consistency()
test_search_existing_contact()
test_delete_existing_contact()
test_deleted_contact_head()
test_deleted_contact_middle()
test_deleted_tail()
