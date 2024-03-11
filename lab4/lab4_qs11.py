current_cart_amount = float(input("Enter the current cart amount: "))
member = input("Are you a member? (yes/no): ")

if member == 'yes':
    if current_cart_amount >= 500:
        discount_rate = 0.15
    elif current_cart_amount >= 300:
        discount_rate = 0.10
    elif current_cart_amount >= 200:
        discount_rate = 0.08
    elif current_cart_amount >= 100:
        discount_rate = 0.04
    else:
        discount_rate = 0.02
else:
    if current_cart_amount >= 500:
        discount_rate = 0.08
    elif current_cart_amount >= 300:
        discount_rate = 0.04
    else:
        discount_rate = 0

final_amount = current_cart_amount - (current_cart_amount * discount_rate)
print(f"Discount rate: {int(discount_rate * 100)}%")
print(f"Final amount to be paid: ${round(final_amount, 2)}")