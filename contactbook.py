contact = {}


def view_contact():
    print("Name\t\tContact Number")
    for key in contact:
        print("{}\t\t{}".format(key,contact.get(key)))

while True:
    choice = int(input(" 1. Add contact \n 2. search contact \n 3. view contact \n 4. update contact \n 5. delete contact \n Enter your choice: "))
    if choice == 1:
        name = input("Enter the contact name ")
        phone = input("Enter the mobile number ")
        contact[name] = phone
    elif choice == 2:
        search_name = input("Enter the contact name: ")
        if search_name in contact:
            print(search_name,"'s contact number is ",contact[search_name])
        else:
            print("Name is not found in contact book")
    elif choice == 3:
        if not contact:
            print("empty contact book")
        else:
            view_contact()
    elif choice == 4:
        update_contact = input("Enter the contact to be update: ")
        if update_contact in contact:
            phone = input("Enter mobile number")
            contact[update_contact]=phone
            print("contact updated")
            view_contact()
        else:
            print("Name is not found in contact book: ")
    elif choice ==5:
        delete_contact = input("Enter the contact to be deleted ")
        if delete_contact in contact:
            confirm = input("Do you want to delete this contact y/n? ")
            if confirm =='y' or confirm =='Y':
                contact.pop(delete_contact)
            view_contact()
        else:
            print("Name is not found in contact book")
    else:
        break                       
