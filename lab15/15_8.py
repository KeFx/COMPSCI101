def get_inventory(filename):
    inventory = {}
    f = open(filename, 'r')
    contents = f.read().strip()
    f.close()
    contents = contents.split('\n')
    contents = contents[1:]

    for line in contents:
        parts = line.split('\t')
        item = parts[0]
        price = float(parts[-1])
        inventory[item] = price
    return inventory

print(get_inventory('file.txt'))