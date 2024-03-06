CNY_to_NZD = 0.22
while True:
    amount_in_nzd = float (input ("Enter an amount in NZD: "))
    amount_in_CNY = amount_in_nzd/CNY_to_NZD
    rounded_amount = round (amount_in_CNY, 2)
    print (amount_in_nzd, "is equivalent to", rounded_amount, "CNY")
    