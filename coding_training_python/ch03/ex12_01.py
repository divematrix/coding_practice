# 연습문제 12. Simple Interest

principal = int(input("Enter the principal: "))

inputRate = float(input("Enter the rate of interest: "))
realRate = inputRate / 100

term = float(input("Enter the number of years: "))

A = principal * (1 + realRate * term)

print("After {:.0f} years at {}%, the investment will be worth ${:.0f}".format(term, inputRate, A))