data = [0, -2, 15, 0, 0, -1, 1, -26]
clean_data = []
count = 0
while count < 5:
    number = data[count]
    if number != 0:
        clean_data += [number]
    count += 1
print(f"Non zero data: {clean_data}")