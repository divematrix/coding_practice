'''
# 연습문제 10. 셀프계산대
	다수의 입력 값으로 금액 계산을 하다 보면 간혹 정확성에 문제가 생기기도 한다.

	간단한 셀프계산대 시스템을 만들어 보자. 세 가지 물건의 가격과 수량을 각각 입력 받은 다음 소계를 구하고 소계에 대한 5.5%의 세금을 계산하자. 그리고 물건 종류별 수량과 전체 수량을 출력한 후 가격 소계, 세금, 합계 금액을 출력하자.

## 출력 예
	- Price of item 1: 25
	- Quantity of item 1: 2
	- Price of item 2: 10
	- Quantity of item 2: 1
	- Price of item 3: 4
	- Quantity of item 3: 1
	- Subtotal: 64.00
	- Tax: 3.52
	- Total: 67.52

## 제약 조건
	- 입력 부분, 계산 부분, 출력 부분을 프로그램에서 모두 구분되게 작성할 것. 즉, 입력 값을 모두 받은 다음 계산을 하고, 출력할 문자열을 생성한 후 최종 결과를 출력하자.
	- 계산을 시작하기 전에 반드시 입력 값을 숫자 데이터로 변환시킬 것

## 도전 과제
	- 입력 값으로 숫자만 받을 수 있도록 프로그램을 수정해보자. 숫자가 입력될 때까지 진행되지 않도록 하라.
	- 제한되지 않은 개수의 물건을 입력 받을 수 있도록 프로그램을 수정해보자. 즉, 물건에 대한 내용이 입력되지 않을 때까지 입력을 받고 세금과 합계 금액을 계산하자.
'''

price_item1 = float(input("price of item 1: "))

quantity_item1 = float(input("Quantity of item 1: "))

price_item2 = float(input("price of item 2: "))

quantity_item2 = float(input("Quantity of item 2: "))

price_item3 = float(input("price of item 3: "))

quantity_item3 = float(input("Quantity of item 3: "))

subtotal = 0
subtotal += price_item1 * quantity_item1
subtotal += price_item2 * quantity_item2
subtotal += price_item3 * quantity_item3

print("Subtotal: %.2f" % subtotal)

tax = 0.055 * subtotal

print("Tax: %.2f" % tax)

total = subtotal + tax

print("Total: %.2f" % total)