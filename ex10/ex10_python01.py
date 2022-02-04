price_item1 = float(input("price of item 1: "))

quantity_item1 = float(input("Quantity of item 1: "))

price_item2 = float(input("price of item 2: "))

quantity_item2 = float(input("Quantity of item 2: "))

price_item3 = float(input("price of item 3: "))

quantity_item3 = float(input("Quantity of item 3: "))

subtotal = 0
subtotal += price_item1 * quantity_item1
subtotal += price_item2 * quantity_item2
subtotal += price_item3 * quantity_item3

print("Subtotal: %.2f" % subtotal)

tax = 0.055 * subtotal

print("Tax: %.2f" % tax)

total = subtotal + tax

print("Total: %.2f" % total)