def calculate_order_total(order, inventory):
    total = 0
    for item, number in order:
        total += inventory[item] * number
    return total