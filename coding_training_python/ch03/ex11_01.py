# 연습문제 11. Currency Conversion

amountfrom = int(input("How many Euros are you exchanging? "))

ratefrom = float(input("What is the exchange rate? "))
rateto = 100

amountto = amountfrom * ratefrom / rateto

print("{} Euros at an exchange rate of {:.2f} is {:.2f} dollars".format(amountfrom, ratefrom, amountto))