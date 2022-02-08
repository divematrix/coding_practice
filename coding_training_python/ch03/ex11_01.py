# 연습문제 11. Currency Conversion

amount_from = float(input("How many Euros are you exchanging? "))

rate_from = float(input("What is the exchange rate? "))
rate_to = 100

amount_to = amount_from * rate_from / rate_to

print("{:.0f} Euros at an exchange rate of {:.2f} is {:.2f} dollars".format(amount_from, rate_from, amount_to))