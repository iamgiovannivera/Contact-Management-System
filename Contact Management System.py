import re

# Define a dictionary to store contacts
contacts = {}

def display_menu():
    print("\nWelcome to the Contact Management System!")
    print("Menu:")
    print("1. Add a new contact")
    print("2. Edit an existing contact")
    print("3. Delete a contact")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Export contacts to a text file")
    print("7. Import contacts from a text file")
    print("8. Quit")

def add_contact():
    identifier = input("Enter unique identifier (phone number or email): ")
    if identifier in contacts:
        print("Contact with this identifier already exists.")
        return
    
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    additional_info = input("Enter additional information (address, notes): ")
    
    if not re.match(r'^\+?\d{10,15}$', phone):
        print("Invalid phone number format.")
        return
    if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
        print("Invalid email address format.")
        return
    
    contacts[identifier] = {
        'Name': name,
        'Phone': phone,
        'Email': email,
        'Additional Info': additional_info
    }
    print("Contact added successfully.")

def edit_contact():
    identifier = input("Enter the unique identifier of the contact to edit: ")
    if identifier not in contacts:
        print("Contact not found.")
        return
    
    print("Enter new details (leave blank to keep current value):")
    name = input(f"Name [{contacts[identifier]['Name']}]: ") or contacts[identifier]['Name']
    phone = input(f"Phone [{contacts[identifier]['Phone']}]: ") or contacts[identifier]['Phone']
    email = input(f"Email [{contacts[identifier]['Email']}]: ") or contacts[identifier]['Email']
    additional_info = input(f"Additional Info [{contacts[identifier]['Additional Info']}]: ") or contacts[identifier]['Additional Info']
    
    if not re.match(r'^\+?\d{10,15}$', phone):
        print("Invalid phone number format.")
        return
    if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
        print("Invalid email address format.")
        return
    
    contacts[identifier] = {
        'Name': name,
        'Phone': phone,
        'Email': email,
        'Additional Info': additional_info
    }
    print("Contact updated successfully.")

def delete_contact():
    identifier = input("Enter the unique identifier of the contact to delete: ")
    if identifier in contacts:
        del contacts[identifier]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def search_contact():
    identifier = input("Enter the unique identifier of the contact to search for: ")
    if identifier in contacts:
        print("Contact details:")
        for key, value in contacts[identifier].items():
            print(f"{key}: {value}")
    else:
        print("Contact not found.")

def display_all_contacts():
    if not contacts:
        print("No contacts available.")
        return
    
    for identifier, details in contacts.items():
        print(f"\nIdentifier: {identifier}")
        for key, value in details.items():
            print(f"{key}: {value}")

def export_contacts():
    filename = input("Enter the filename to export contacts to: ")
    with open(filename, 'w') as file:
        for identifier, details in contacts.items():
            file.write(f"Identifier: {identifier}\n")
            for key, value in details.items():
                file.write(f"{key}: {value}\n")
            file.write("\n")
    print("Contacts exported successfully.")

def import_contacts():
    filename = input("Enter the filename to import contacts from: ")
    try:
        with open(filename, 'r') as file:
            content = file.read().strip()
            entries = content.split("\n\n")
            for entry in entries:
                lines = entry.split("\n")
                identifier = lines[0].split(": ")[1]
                name = lines[1].split(": ")[1]
                phone = lines[2].split(": ")[1]
                email = lines[3].split(": ")[1]
                additional_info = lines[4].split(": ")[1]
                
                contacts[identifier] = {
                    'Name': name,
                    'Phone': phone,
                    'Email': email,
                    'Additional Info': additional_info
                }
        print("Contacts imported successfully.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    while True:
        display_menu()
        choice = input("Select an option (1-8): ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            edit_contact()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            search_contact()
        elif choice == '5':
            display_all_contacts()
        elif choice == '6':
            export_contacts()
        elif choice == '7':
            import_contacts()
        elif choice == '8':
            print("Thank you for using the Contact Management System. Goodbye!")
            break
        else:
            print("Invalid option. Please select a number between 1 and 8.")

if __name__ == "__main__":
    main()