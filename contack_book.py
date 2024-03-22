contacts = []  # List to store contacts as dictionaries

def display_contact():
  
  if not contacts:
    print("There are no contacts saved yet.")
    return
  print("-" * 40)
  print("| Name          | Phone Number  | Email          | Address       |")
  print("-" * 80)
  for contact in contacts:
    print(f"| {contact['name']:<15} | {contact['phone_number']:<15} | {contact['email']:<15} | {contact['address']:<20} |")
  print("-" * 80)

while True:
  choice = int(input("Menu:\n1. Add new contact\n2. Search contact\n3. Display contact list\n4. Update contact\n5. Delete contact\n6. Exit\nEnter your choice: "))

  if choice == 1:
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email (optional): ")
    address = input("Enter address (optional): ")
    contact = {"name": name, "phone_number": phone, "email": email, "address": address}
    contacts.append(contact)
    print("Contact added successfully!")

  elif choice == 2:
    search_name = input("Enter the contact name to search: ")
    found = False
    for contact in contacts:
      if search_name.lower() in contact["name"].lower():
        print("-" * 40)
        print("| Name          | Phone Number  | Email          | Address       |")
        print("-" * 80)
        print(f"| {contact['name']:<15} | {contact['phone_number']:<15} | {contact['email']:<15} | {contact['address']:<20} |")
        print("-" * 80)
        found = True
        break
    if not found:
      print("Name not found in contact book.")

  elif choice == 3:
    display_contact()

  elif choice == 4:
    update_name = input("Enter the name of the contact to update: ")
    found = False
    for i, contact in enumerate(contacts):
      if update_name.lower() in contact["name"].lower():
        name = input("Update name (or leave blank): ") or contact["name"]
        phone = input("Update phone number (or leave blank): ") or contact["phone_number"]
        email = input("Update email (or leave blank): ") or contact["email"] if contact["email"] else ""
        address = input("Update address (or leave blank): ") or contact["address"] if contact["address"] else ""
        contacts[i] = {"name": name, "phone_number": phone, "email": email, "address": address}
        print("Contact updated successfully!")
        found = True
        break
    if not found:
      print("Name not found in contact book.")

  elif choice == 5:
    del_name = input("Enter the name of the contact to delete: ")
    found = False
    for i, contact in enumerate:
      if del_name.lower() in contact["name"].lower():
        del contacts[i]
        print("Contact deleted successfully!")
        found = True
        break
