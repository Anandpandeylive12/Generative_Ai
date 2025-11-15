def calculate_bill(cups,price_per_cup):
    total = cups * price_per_cup
    return total

my_Bill = calculate_bill(3,5)
print("Total bill amount is:", my_Bill)