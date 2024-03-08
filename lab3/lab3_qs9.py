numerator = int(input("Enter the numerator: "))
denominator = int(input("Enter the denominator: "))

if denominator == 0:
    result = 'Undefined'
else:
    result = round((numerator/denominator),2)

print(f"Result: {result}")