contacts = []

while True:
    print("\n----- CONTACT BOOK -----")
    print("1. View Contacts")
    print("2. Add Contact")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        if len(contacts) == 0:
            print("No contacts found.")
        else:
            print("\nContacts:")
            i = 1
            for contact in contacts:
                print(str(i) + ". Name:", contact[0], "| Phone:", contact[1])
                i = i + 1

    elif choice == "2":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contacts.append([name, phone])
        print("Contact added.")

    elif choice == "3":
        name = input("Enter name to search: ")
        found = False

        for contact in contacts:
            if contact[0] == name:
                print("Name:", contact[0])
                print("Phone:", contact[1])
                found = True

        if found == False:
            print("Contact not found.")

    elif choice == "4":
        name = input("Enter name to update: ")
        found = False

        for contact in contacts:
            if contact[0] == name:
                contact[0] = input("Enter new name: ")
                contact[1] = input("Enter new phone number: ")
                print("Contact updated.")
                found = True

        if found == False:
            print("Contact not found.")

    elif choice == "5":
        name = input("Enter name to delete: ")
        found = False

        for contact in contacts:
            if contact[0] == name:
                contacts.remove(contact)
                print("Contact deleted.")
                found = True
                break

        if found == False:
            print("Contact not found.")

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")