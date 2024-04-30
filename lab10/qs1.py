low = int(input("Enter the lower bound: "))
upp = int(input("Enter the upper bound: "))

l = []

for i in range(low, upp+1):
    if (i % 3 == 0) or (i % 5 == 0):
        l.append(i)

print(f"Sum of multiples within [{low}, {upp}] is {sum(l)}.")