def get_smallest(code_dictionary):
    min_code = min(code_dictionary)
    return sorted(code_dictionary[min_code])[0]