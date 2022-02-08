# 연습문제 10. 셀프계산대 Self Counter

price_item1 = float(input("Price of item 1: "))

quantity_item1 = float(input("Quantity of item 1: "))

price_item2 = float(input("Price of item 2: "))

quantity_item2 = float(input("Quantity of item 2: "))

price_item3 = float(input("Price of item 3: "))

quantity_item3 = float(input("Quantity of item 3: "))

subtotal = 0
subtotal += price_item1 * quantity_item1
subtotal += price_item2 * quantity_item2
subtotal += price_item3 * quantity_item3

tax = 0.055 * subtotal

total = subtotal + tax

print("Subtotal: ${:.2f}".format(subtotal))

print("Tax: ${:.2f}".format(tax))

print("Total: ${:.2f}".format(total))