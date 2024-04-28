start = int(input("Enter the range start: "))
end = int(input("Enter the range end: "))

invalid_total = 0

while True: 
    uin = int(input(f"Enter an integer between {start} and {end} (inclusive): "))
    if start <= uin <= end:
        break
    invalid_total += uin

print(f"The total of all the invalid integers is {invalid_total}.")