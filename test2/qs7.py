list2 = []
uin = int(input(f"Enter an integer: "))

for i in list_numbers:
    if i % uin != 0:
        list2.append(i)

if len(list2) == len(list_numbers):
    print(f"There is no multiple of {uin} in the list!")
print(f"Resulting list: {list2}")