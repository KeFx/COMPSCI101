u_int = int(input("Enter an integer: "))
s = 0

for i in range(2, u_int, 2): 
    s += i

print(f"The result of the sum is {s}.")