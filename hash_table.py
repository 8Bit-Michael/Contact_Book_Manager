class Node: # Linked list node for handling collisions
    def __init__(self, contact, next_node=None):
        self.contact = contact
        self.next = next_node
    
class HashTable:
    def __init__(self, size):
        self.size = size
        # initialize empty buckets and multiply based on size int
        self.buckets = [None] * size

    def add_contact(self, name, number, email): 
        contact = {"name": name, "number": number, "email": email} # create contact dictionary
        node = name.strip('"')
        node = Node(
            contact = contact # initialize contact
        ) 
        index = self.hash_function(node.contact["name"]) # create hash index
        bucket = self.hashtable.buckets[index] = [node] # assign node to that index
        if bucket: # If bucket =! empty or not None
            for i, item in enumerate(bucket): # Iterate through contacts in the bucket
                # support Node objects or plain dicts
                contact = item.contact if hasattr(item, "contact") else item
                bucket.append[i] # append at that exact index
                return f"{node.contact["name"]} appended at bucket index {index}" # otherwise just append
        else: # if bucket = empty
            bucket.append(contact) # append bucket
            return f"{node.contact["name"]} appended at bucket index {index}" # return string

    def hash_function(self, key):
        # the sum of the ASCII values of the characters in the key divided by the number of buckets
        # giving you a randomized index that is still within the bounds of the array
        if self.buckets:
            return sum(ord(char) for char in key) % len(self.buckets)
        else:
            return "Error: Hash table size is None."

    def search_contact(self, name):
        hash_index = self.hash_function(name) # Get hash index with name as key
        bucket = self.buckets[hash_index] # Retrieve the bucket at that index
        if bucket: # If bucket is not empty or not None
            for i, item in enumerate(bucket): # Iterate through contacts(indexes) in the bucket
                # support Node objects or plain dicts
                contact = item.contact if hasattr(item, "contact") else item
                if contact.get("name") == name: # If contact node's contact dictionary is equal to name
                    return f"{name} found at index {hash_index}, position {i}" # Return the contact with position

    def delete_contact(self, name):
        hash_index = self.hash_function(name) # Get hash index with name as key
        bucket = self.buckets[hash_index] # Retrieve the bucket at that index
        if bucket: # If bucket is not empty or not None
            for i, item in enumerate(bucket): # Iterate through contacts in the bucket
                # support Node objects or plain dicts
                contact = item.contact if hasattr(item, "contact") else item
                if contact.get("name") == name: # If contact name matches
                    del bucket[i]
                    return f"{name} deleted from index {hash_index}, position {i}" 
                    # Delete the contact
                    # keep an empty list instead of None so tests can check length

    def display_all(self, bucket_index): # let the user insert a key
        bucket = self.buckets[bucket_index] # look for bucket at that index
        if bucket:
            # for the index of each contact in the bucket
            for i, item in enumerate(bucket):
                contact = item.contact if hasattr(item, "contact") else item
                print(f"Index {i}: {contact}") # print the contact details
        else:
            print("Error: No contacts found.")

    def get_load_factor(self): # Calculate how much the hash table is filled
        if self.buckets:
            #  count only non-empty buckets (truthy lists), not just non-None
            filled_buckets = sum(1 for bucket in self.buckets if bucket)
            # divide that by total number of buckets to get load factor(0 to 1)
            return filled_buckets / len(self.buckets) if len(self.buckets) > 0 else 0
        else:
            print("Error: No contacts found.")
