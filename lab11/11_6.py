def perform_currency_exchange(currency_list, rate_list):
    user_selection = get_user_selection()
    while user_selection != 0:
        nz_dollar_amount = float(input("Enter the amount of NZ dollars you want to convert: "))
        if user_selection != 7:
            exchange_amount = round(nz_dollar_amount * rate_list[user_selection - 1], 2)
        else:
            exchange_amount = round(nz_dollar_amount * rate_list[user_selection - 1])
        print(f"${nz_dollar_amount} NZ dollars = ${exchange_amount} {currency_list[user_selection - 1]}")
        user_selection = get_user_selection()