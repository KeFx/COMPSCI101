import math
amount_to_retrieve = int(input("Enter an amount: "))

if (amount_to_retrieve < 50) or (amount_to_retrieve > 500) or ((amount_to_retrieve % 10) != 0):
    print("Invalid amount.")
else:
    print(f"Thank you. You will receive {math.floor(amount_to_retrieve/50)} bill(s) of 50 and {round((amount_to_retrieve%50)/10)} bill(s) of 10.")