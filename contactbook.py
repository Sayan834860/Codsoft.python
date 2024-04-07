contact = {}
def view_contact():
    print("Name\t\tContact Number")
    for key in contact:
        print("{}\t\t{}" .format(key,contact.get(key)))
while True:
    choice=int(input(" 1.Add Contact\n 2.Search contact\n 3.View Contact List\n 4.Update Contact\n 5.Delete Contact\n 6.Exit\n Enter your choice: "))
    if choice == 1:
        name=input("Enter the contact name: ")
        phone=int(input("Enter the contact mobile number: "))
        contact[name] = phone
    elif choice == 2:
        search_name = input("Enter contact name: ")
        if search_name in contact:
            print(search_name,"contact number is",contact[search_name])
        else:
            print("name is not found in contact book")
    elif choice == 3:
        if not contact:
            print("Empty contact book")
        else:
            view_contact()
    elif choice == 4:
        update_contact=input("Enter the contact to be updated: ")
        if update_contact in contact:
            phone=int(input("Enter mobile number: "))
            contact[update_contact]=phone
            print("contact updated")
            view_contact()
        else:
            print("name is not found in contact book")
    elif choice == 5:
        delete_contact=input("Enter the contact to be deleted: ")
        if delete_contact in contact:
            confirm=input("if you want to delete this contact(yes/no): ")
            if confirm == 'yes':
                contact.pop(delete_contact)
            view_contact()
        else:
            print("name is not found in contact book")
    elif choice == 6:
        print("Exit....")
        break
    else:
        print("Error...")

