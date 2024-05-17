def process_transactions(filename):
    f = open(filename, 'r')
    name_on_first_line = f.readline().strip()
    transactions = f.read().split('\n')
    f.close()
    total = 0
    for transaction in transactions:
        colon_index = transaction.index(':')
        transaction_name = transaction[:colon_index]
        transaction_amount = transaction[colon_index+1:]
        if transaction_name == name_on_first_line:
            total += int(transaction_amount)
    return (name_on_first_line, total)

print(process_transactions('13_8_transactions.txt'))