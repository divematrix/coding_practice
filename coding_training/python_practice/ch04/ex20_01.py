# 연습문제 20. 여러 주를 지원하는 세금 계산기

# 주문 가격 입력 받기
order_amount = float(input("What is the order amount? "))

state_tax = float()
state_tax_rate = float()
county_tax = float()
county_tax_rate = float()

# 주문할 주 입력 받기
state = input("What state do you live in? ")
county = ''
tax_rate = float()

# - 위스콘신 주의 경우 카운티 추가 입려 받기
#   - Eau Claire 카운티 0.005의 세금
#   - Dunn 카운티 0.004의 세금
# - 일리노이 주의 경우 8% 세금 - 카운티 세금 없음

if state == 'Wisconsin':
	county = input("What county do you live in? ")
	state_tax_rate = 0.055
	if county == 'Eau Claire':
		county_tax_rate = 0.005
	elif county == 'Dunn':
		county_tax_rate = 0.004
	else:
		county_tax_rate = 0
elif state == 'Illinois':
	state_tax_rate = 0.08
	county_tax_rate = 0
else:
	state_tax_rate = 0
	county_tax_rate = 0

# 출력
# - 위스콘신, 일리노이: 세금과 세금이 포함된 총 금액
# - 나머지: 세금이 포함된 총 금액

# 계산
state_tax = order_amount * state_tax_rate

county_tax = order_amount * county_tax_rate

total_tax = state_tax + county_tax

total = order_amount + total_tax

# 출력
print(("The state tax is ${:.2f}\nThe county tax is ${:.2f}\nThe total tax is ${:.2f}\n".format(state_tax, county_tax, total_tax) if state == 'Wisconsin' or state == 'Illinois' else "") + "The total is ${:.2f}".format(total))