print(f"The given list is: {data}")

while True:
    uin = int(input("Enter an integer from the given list: "))
    if uin in data: 
        print(f"{uin} is valid.")
        break