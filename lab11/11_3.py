def print_menu(currency_list, rate_list):
    print("Select an operation:")
    print(f"Enter 1 to exchange NZ Dollars to {currency_list[0]} " 
          f"(1 NZD = {rate_list[0]} {currency_list[0]})")
    print(f"Enter 2 to exchange NZ Dollars to {currency_list[1]}" 
          f"(1 NZD = {rate_list[1]} {currency_list[1]})")
    print(f"Enter 3 to exchange NZ Dollars to {currency_list[2]}" 
          f"(1 NZD = {rate_list[2]} {currency_list[2]})")
    print(f"Enter 4 to exchange NZ Dollars to {currency_list[3]}" 
          f"(1 NZD = {rate_list[3]} {currency_list[3]})")
    print(f"Enter 5 to exchange NZ Dollars to {currency_list[4]}" 
          f"(1 NZD = {rate_list[4]} {currency_list[4]})")
    print(f"Enter 6 to exchange NZ Dollars to {currency_list[5]}" 
          f"(1 NZD = {rate_list[5]} {currency_list[5]})")
    print(f"Enter 7 to exchange NZ Dollars to {currency_list[6]}" 
          f"(1 NZD = {rate_list[6]} {currency_list[6]})")
    print("Enter 0 to exit the currency converter")
    print()

	
currency_list = ["Pound Sterling", "US Dollars", "Euros", "Canadian Dollars", "Australian Dollars", "Singaporean Dollars", "Japanese Yen"]
rate_list = [0.52, 0.62, 0.58, 0.84, 0.92, 0.84, 84.43]
print_menu(currency_list, rate_list)