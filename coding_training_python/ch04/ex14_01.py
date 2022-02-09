# 연습문제 14. 세금 계산기 Tax Calculator

order_amount = float(input("What is the order amount? "))

state = input("What is the state? ")

subtotal = order_amount

tax = 0.055 * subtotal

total = subtotal + tax

result = ""

if state == 'WI':
	result += "The subtotal is ${:.2f}\nThe tax is ${:.2f}\n".format(subtotal, tax)

result += "The total is ${:.2f}".format(total)

print(result)