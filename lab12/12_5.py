def carry_out_transactions(balance, transactions_tuple):
    net_transaction = sum(transactions_tuple)
    balance += net_transaction
    
    total_deposits = get_total_deposits(transactions_tuple)
    total_withdrawals = get_total_withdrawals(transactions_tuple)

    return balance, total_deposits, total_withdrawals

def get_total_deposits(transactions_tuple):
    total = 0
    for transaction in transactions_tuple:
        if transaction > 0:
            total += transaction
    return total

def get_total_withdrawals(transactions_tuple):
    total = 0
    for transaction in transactions_tuple:
        if transaction < 0:
            total += -(transaction)
    return total


results = carry_out_transactions(5400, (100, -400, 500, 
-800, 600, -100, - 200, 50, 0, -200))
print("Balance $", results[0], ", deposits $", results[1], 
", withdrawals $", results[2], sep="")
