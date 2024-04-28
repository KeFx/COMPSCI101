i = input("Enter a line of integers: ")
l = list(map(int, i.split(",")))

maxNum = 0
minNum = 0

for idx in range(len(l)):
    if idx == 0: 
        maxNum = l[idx]
        minNum = l[idx]
    elif l[idx] > maxNum:
        maxNum = l[idx]
        print(f"Assigned maxNum to {maxNum}")
    elif l[idx] < minNum:
        minNum = l[idx]
        print(f"Assigned minNum to {minNum}")

print(f"The minimum number is {minNum} and the maximum number is {maxNum}.")