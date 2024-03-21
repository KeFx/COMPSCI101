factor = int(input("Enter a factor: "))
maximum = int(input("Enter a maximum: "))
total = 0
counter  = 1

while counter <= maximum :
    if counter % factor == 0 :
        total += counter
    counter += 1

print(f"The sum of the multiples of {factor} between 1 and {maximum} is equal to {total}.")

