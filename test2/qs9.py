data = "hi how are you "
list_data = []
pos = 0

for i in range(len(data)):
    if data[i] == " ":
       list_data.append(data[pos:i])
       pos = i
list_data.append(data[pos:i+1])

print(len(list_data))