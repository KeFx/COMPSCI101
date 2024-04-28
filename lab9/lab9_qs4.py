first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
start = min((first, second))
stop = max((first, second)) + 1
for i in range(start, stop, 1):
    print(i, end=' ')