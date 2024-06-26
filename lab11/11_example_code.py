currency_list = ["Pound Sterling", "US Dollars", "Euros", "Canadian Dollars", "Australian Dollars", "Singaporean Dollars", "Japanese Yen"]
rate_list = [0.52, 0.62, 0.58, 0.84, 0.92, 0.84, 84.43]
banner_text = "A Currency Converter"
print("*" * (len(banner_text) + 2))
print("*" + banner_text + "*")
print("*" * (len(banner_text) + 2))
print()
print("Select an operation:")
print(f"Enter 1 to exchange NZ Dollars to {currency_list[0]} (1 NZD = {rate_list[0]} {currency_list[0]})")
print(f"Enter 2 to exchange NZ Dollars to {currency_list[1]} (1 NZD = {rate_list[1]} {currency_list[1]})")
print(f"Enter 3 to exchange NZ Dollars to {currency_list[2]} (1 NZD = {rate_list[2]} {currency_list[2]})")
print(f"Enter 4 to exchange NZ Dollars to {currency_list[3]} (1 NZD = {rate_list[3]} {currency_list[3]})")
print(f"Enter 5 to exchange NZ Dollars to {currency_list[4]} (1 NZD = {rate_list[4]} {currency_list[4]})")
print(f"Enter 6 to exchange NZ Dollars to {currency_list[5]} (1 NZD = {rate_list[5]} {currency_list[5]})")
print(f"Enter 7 to exchange NZ Dollars to {currency_list[6]} (1 NZD = {rate_list[6]} {currency_list[6]})")
print("Enter 0 to exit the currency converter")
print()
user_selection = int(input("Enter your selection: "))
while user_selection < 0 or user_selection > 7:
    print("Invalid selection!")
    user_selection = int(input("Enter your selection: "))
while user_selection != 0:
    nz_dollar_amount = float(input("Enter the amount of NZ dollars you want to convert: "))
    if user_selection != 7:
        exchange_amount = round(nz_dollar_amount * rate_list[user_selection - 1], 2)
    else:
        exchange_amount = round(nz_dollar_amount * rate_list[user_selection - 1])
    print(f"${nz_dollar_amount} NZ dollars = ${exchange_amount} {currency_list[user_selection - 1]}")
    user_selection = int(input("Enter your selection: "))
    while user_selection < 0 or user_selection > 7:
        print("Invalid selection!")
        user_selection = int(input("Enter your selection: "))
print()
print("Exiting the currency converter...")
print("Have a good day!")