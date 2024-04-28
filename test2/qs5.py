import math
while True :
    uin = int(input("Enter a square number: "))

    if math.sqrt(uin).is_integer():
        print(f"{uin} is the square of {round(math.sqrt(uin))}.")
        break
