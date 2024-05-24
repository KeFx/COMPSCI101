def create_baby_names_dictionary(filename):
    f = open(filename, 'r')
    names = f.read().split()
    f.close()
    
    baby_names_dict = {}
    names.sort()
    for name in names:
        if name[0] in baby_names_dict:
            baby_names_dict[name[0]].append(name)
        else:
            baby_names_dict[name[0]] = [name]
    return baby_names_dict

def print_baby_names(baby_names_dict):
    for letter, names in baby_names_dict.items():
        print(letter + ':', ' '.join(names))

baby_names_dict = create_baby_names_dictionary('f.txt')
print_baby_names(baby_names_dict)