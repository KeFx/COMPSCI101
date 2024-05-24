def update_dictionary(a_dict, target_value):
    for key, value in list(a_dict.items()):
        if value == target_value:
            del a_dict[key]