def print_banner():
    banner_text = "A Currency Converter"
    print("*" * (len(banner_text) + 2))
    print("*" + banner_text + "*")
    print("*" * (len(banner_text) + 2))

def print_menu(currency_list, rate_list):
    print("Select an operation:")
    print(f"Enter 1 to exchange NZ Dollars to {currency_list[0]} " 
          f"(1 NZD = {rate_list[0]} {currency_list[0]})")
    print(f"Enter 2 to exchange NZ Dollars to {currency_list[1]} " 
          f"(1 NZD = {rate_list[1]} {currency_list[1]})")
    print(f"Enter 3 to exchange NZ Dollars to {currency_list[2]} " 
          f"(1 NZD = {rate_list[2]} {currency_list[2]})")
    print(f"Enter 4 to exchange NZ Dollars to {currency_list[3]} " 
          f"(1 NZD = {rate_list[3]} {currency_list[3]})")
    print(f"Enter 5 to exchange NZ Dollars to {currency_list[4]} " 
          f"(1 NZD = {rate_list[4]} {currency_list[4]})")
    print(f"Enter 6 to exchange NZ Dollars to {currency_list[5]} " 
          f"(1 NZD = {rate_list[5]} {currency_list[5]})")
    print(f"Enter 7 to exchange NZ Dollars to {currency_list[6]} " 
          f"(1 NZD = {rate_list[6]} {currency_list[6]})")
    print("Enter 0 to exit the currency converter")
    print()

def get_user_selection():
    user_selection = int(input("Enter your selection: "))
    while user_selection < 0 or user_selection > 7:
        print("Invalid selection!")
        user_selection = int(input("Enter your selection: "))
    return user_selection

def perform_currency_exchange(currency_list, rate_list):
    user_selection = get_user_selection()
    while user_selection != 0:
        nz_dollar_amount = request_conversion_amount_nzd()
        converted_amount = nz_dollar_amount * rate_list[user_selection - 1]
        if user_selection != 7:
            exchange_amount = round(converted_amount, 2)
        else:
            exchange_amount = round(converted_amount)
            
        print_conversion(
            nz_dollar_amount, 
            exchange_amount, 
            currency_list[user_selection - 1]
        )

        user_selection = get_user_selection()

def request_conversion_amount_nzd():
    request_nzd_amount_prompt = ("Enter the amount of NZ dollars "
                                 "you want to convert: ")
    return float(input(request_nzd_amount_prompt))

def print_conversion(nzd_amount, exchange_amount, target_currency):
    print(f"${nzd_amount} NZ dollars = ${exchange_amount} {target_currency}")

def print_exit_message():
    print("Exiting the currency converter...")
    print("Have a good day!")

def main():
    currency_list = [
        "Pound Sterling", 
        "US Dollars", 
        "Euros", 
        "Canadian Dollars",
        "Australian Dollars", "Singaporean Dollars", "Japanese Yen"]
    rate_list = [0.52, 0.62, 0.58, 0.84, 0.92, 0.84, 84.43]
    print_banner()
    print()
    print_menu(currency_list, rate_list)
    perform_currency_exchange(currency_list, rate_list)
    print()
    print_exit_message()