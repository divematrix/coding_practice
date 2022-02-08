# 연습문제 12. 단리 계산 Simple Interest

principal = float(input("Enter the principal: "))

interest_Rate_annual_percent = float(input("Enter the rate of interest: "))
interest_Rate_annual = interest_Rate_annual_percent / 100

term_annual = float(input("Enter the number of years: "))

principal_and_interest = principal * (1 + interest_Rate_annual * term_annual)

print("After {:.0f} years at {}%, the investment will be worth ${:.0f}".format(term_annual, interest_Rate_annual_percent, principal_and_interest))