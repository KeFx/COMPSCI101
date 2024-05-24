def merge_dictionaries(email_dict, phone_num_dict):
    contacts_dict = {}
    for name in email_dict:
        contacts_dict[name] = (email_dict[name], phone_num_dict[name])
    return contacts_dict