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