from hash_table import HashTable, Node
from difflib import get_close_matches

def match_input(user_input, options, cutoff=0.6):
    return get_close_matches(user_input.lower(), options, n=1, cutoff=cutoff)
    
def main():
    hashtable = HashTable(size=10)

    while True:
        command = input("""Enter a command:
        1. Create contact
        2. Delete contact
        3. Search contact
        4. Display all
        5. Load factor
        0. Exit
        """)

        #  {"name": "Alice", "phone_number": "555-1234", "email": "alice.@example.com"} 
        if match_input(command, ['Create contact', '1']):
            name = input("Enter your contact name/key: ")
            number = input("Enter your contact phone number: ")
            email = input("Enter your contact email: ")
            result = hashtable.add_contact(name, number, email)
            print(result)
        
        elif match_input(command, ['Delete contact', '2']):
            name = input("Insert deletion key: ")
            result = hashtable.delete_contact(name)
            return(result)

        elif match_input(command, ['Search contact', '3']):
            name = input("Insert key to search: ")
            result = hashtable.search_contact(name)
            return(result)
        
        elif match_input(command, ['Display all contacts', '4']):
            bucket_index = input("Insert bucket index: ")
            result = hashtable.display_all(bucket_index)
            print(result)

        elif match_input(command, ['Load factor', '5']):
           result = hashtable.get_load_factor()
           print(f'Load factor {result}')

        elif match_input(command, ['exit', '0']):
            print("Exiting the application.")
            exit(0)

        else:
            matches = match_input(command, 
            ['create contacts', 'delete contact', 'search contact', 'display all contacts', 
            'load factor', 'exit', '1', '2', '3', '4', '5', '0'])
            if matches:
                command = input(f"Did you mean '{matches[0]}'?")
                print("Returning to menu...")
                return
            else:
                print("Unknown command. Please try again.")
                return


while __name__ == '__main__':
    main()
