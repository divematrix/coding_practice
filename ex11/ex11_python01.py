euro = int(input("How many Euros are you exchanging? "))

exRate = float(input("What is the exchange rate? "))

exDollar = euro * exRate / 100

# 자리수 조절
def toCeil(number, underpoint):
	if type(underpoint) != type(1):
		return False

	number *= 10 ** underpoint

	import math
	number = math.ceil(number)
	
	number /= 10 ** underpoint
	
	return number

exDollar = toCeil(exDollar, 2)

print("{} Euros at an exchange rate of {} is {} dollars".format(euro, exRate, exDollar))