def main():
    contact_list = get_contacts("Contacts1.txt")
    display_menu()
    
    print()
    
    user_select = get_user_selection()
    while user_select != 3:
        if user_select == 1:
            contact_name = input("Enter contact's name: ")
            contact_info = get_contact_info(contact_list, contact_name)
            
            print()
            print_contact_info(contact_info)
            print()
        else:
            add_contact(contact_list)
            
        user_select = get_user_selection()

    save_contacts(contact_list, 'khu772.txt')
    
    print("Exiting program ... goodbye!")
        
def display_menu():
    print(
        f"***********************\n"
        f"Simple Contacts Program\n"
        f"***********************\n"
        f"1. Display contact info\n"
        f"2. Add a new contact\n"
        f"3. Save and Exit\n"
        )

def get_user_selection():
    valid_selections = [1, 2, 3]
    prompt = "Enter selection: "
    u_select = int(input(prompt))
    while u_select not in valid_selections:
        print("Invalid input!")
        u_select = int(input(prompt))
    return u_select

def get_contacts(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()
    contact_list = []
    for idx in range(0, len(lines), 3):
        name = lines[idx].strip()
        mobile = lines[idx+1].strip()
        email = lines[idx+2].strip()
        contact_list.append((name, mobile, email))
    return contact_list
        
def get_contact_info(contact_list, contact_name):
    for contact in contact_list:
        if contact[0] == contact_name:
            return contact

def print_contact_info(contact_info):
    if contact_info != None:
        name = contact_info[0]
        phone = contact_info[1]
        email = contact_info[2]
        print(f"Name: {name} Phone: {phone} Email: {email}")
    else:
        print("Contact not found")

def add_contact(contact_list):
    print("Please enter the new contact's details")
    name = input("Contact's Name: ")
    phone = input("Contact's Phone Number: ")
    email = input("Contact's Email address: ")
    print("Contact added")
    contact_list.append((name, phone, email))

def save_contacts(contact_list, filename):
    f = open(filename, 'w')
    for contact in contact_list:
        for line in contact:
            f.write(line + '\n')
    f.close()
