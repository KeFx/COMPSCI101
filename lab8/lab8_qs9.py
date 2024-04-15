l = []
l2 = []

while True :
    user_input = input("Enter a value or stop to end: ")
    if user_input != 'stop':
        l.append(float(user_input))
    else: 
        break

thresh = float(input("Enter a threshold value: "))

for value in l: 
    if value > thresh: 
        l2.append(value)

print(f"The average of the values greater than {thresh} is {round(sum(l2)/len(l2), 2)}")
