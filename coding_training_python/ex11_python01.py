'''
# 연습문제 11. 환율 변환
	때에 따라서는 환율을 다루는 경우도 생길 것이다. 이 경우 최대한 정확하게 계산되도록 해야 한다.
	환율을 변환하는 프로그램을 작성하라. 여기에서는 유로에서 미국 달러로 변환시킨다.
	먼저 유로 금액을 입력 받은 다음 유로 환율을 입력 받는다.
	그리고는 유로에 해당하는 미국 달러 값을 출력한다. 환율 변환식은 다음과 같다.
		- amount to는 변환될 미국 달러 가격이다.
		- amount from은 유로 가격이다.
		- rate from은 현재의 유로 환율이다.
		- rate to는 현재의 미국 달러 환율이다.

## 출력 예
	- How many Euros are you exchanging? 81
	- What is the exchange rate? 137.51
	- 81 Euros at an exchange rate of 137.51 is 111.38 dollars

## 제약 조건
	- 센트를 기준으로 하는 소숫점 다음에 숫자가 있을 때는 센트를 기준으로 올림 처리를 할 것
	- 한 개의 출력문만 사용할 것

## 도전 과제
	- 환율표를 프로그램에 넣은 다음 환율 대신 국가 이름을 입력 받도록 프로그램을 수정해보자.
	- 애플리케이션에 별도의 API를 적용하여 현재의 업데이트된 환율을 적용하는 프로그램으로 수정해보자.
'''

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