user_input = input("Enter a line of integer values: ")
l = user_input.split(",")
even_list = []

for i in l: 
    num = int(i)
    if num % 2 == 0:
        even_list.append(str(num))

print(f"The even integers are: {', '.join(even_list)}")