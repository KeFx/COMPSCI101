prices = input("Enter a list of apartment prices: ").split(',')
bedroom_num = input("Enter a list of numbers of bedrooms: ").split(',')
l12 = []
l34 = []

for i in range(len(bedroom_num)):
    if bedroom_num[i] == '1' or bedroom_num[i] == '2':
        l12.append(int(prices[i]))
    else:
        l34.append(int(prices[i]))

if len(l12) == 0:
    print(f"There is no apartment with 1 or 2 bedrooms in the list.")
else :
    print(f"The average price for apartments with 1 or 2 bedrooms is ${round(sum(l12)/len(l12))}.")
if len(l34) == 0:
    print(f"There is no apartment with 3 or 4 bedrooms in the list.")   
else :
    print(f"The average price for apartments with 3 or 4 bedrooms is ${round(sum(l34)/len(l34))}.")