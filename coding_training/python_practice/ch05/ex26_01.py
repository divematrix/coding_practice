# 연습문제 26. 카드 대금 상환 기간

import math

total_balance = float(input("What is your balance? "))

annual_percentage_Rate = float(input("What is the APR on the card (as a percent)? "))

month_repayment = float(input("What is the monthly payment you can make? "))


def calculateMonthsUntilPaidOff (b, apr, p):
	import math

	rate_month = math.pow(1 + apr / 100, 1 / 12) -1

	n = -1 * math.log(1 - b * rate_month / p) / math.log(1 + rate_month)

	return n

print("It will take you {} months to pay off this card".format(math.ceil(calculateMonthsUntilPaidOff(total_balance, annual_percentage_Rate, month_repayment))))