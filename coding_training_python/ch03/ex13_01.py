# 연습문제 13. 복리 계산 Compound Interest

principal = float(input("What is the principal amount? "))

interest_Rate_annual_percent = float(input("What is the rate: "))

interest_Rate_annual = interest_Rate_annual_percent / 100

term_annual = float(input("What is the number of years: "))

interest_times_per_year = float(input("What is the number of times the interest is compounded per year: "))

principal_and_interest = principal * (1 + interest_Rate_annual / interest_times_per_year) ** (interest_times_per_year * term_annual)

print("${:.0f} invested at {}% for {:.0f} years compounded {:.0f} times per year is ${:.2f}".format(principal, interest_Rate_annual_percent, term_annual, interest_times_per_year, principal_and_interest))