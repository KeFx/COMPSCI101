list = []

while True :
    u_in = input("Please enter a positive integer or end to stop: ")
    if u_in.isnumeric(): 
        u_in = int(u_in)
        if u_in > 0 :
            list.append(u_in)
    elif u_in == "end" :
        break

list.sort()
list.reverse()
print(f"Positive numbers: {list}")
