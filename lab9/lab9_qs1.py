i = input("Please enter a line of integers: ")
l = list(map(int, i.split(",")))
even_l = []

for n in l: 
    if n % 2 == 0:
        even_l.append(n)

if len(even_l) != 0: 
    print(f"The average of the even numbers is {round(sum(even_l)/len(even_l), 2)}.")
else:
    print('The average of the even numbers is undefined.')