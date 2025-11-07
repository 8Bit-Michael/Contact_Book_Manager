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
