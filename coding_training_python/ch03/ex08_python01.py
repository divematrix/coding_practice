'''
# 연습문제 08. 피자 파티
	나눗셈은 항상 딱 떨어지지만은 않기 때문에 종종 소수 대신 몫과 나머지를 다루는 프로그램을 작성해야 할 때도 있다. 피자를 정확하게 나누는 프로그램을 작성하라. 사람 수, 피자 개수,조각 개수를 입력 받는데, 이때 조각 개수는 짝수여야 한다. 일단 한 사람이 받게 되는 피자 조각 개수를 출력해보자. 만일 남는 조각이 있다면 그 개수도 나타내보자.

## 출력 예
	- How many people? 8
	- How many pizzas do you have? 2
	- How many pieces are in a pizza? 8
	- 8 people with 2 pizzas
	- Each person gets 2 pieces of pizza.
	- There are 0 leftover pieces.

## 도전 과제
	- 입력 값으로 숫자만 받을 수 있도록 프로그램을 수정해보자. 숫자가 입력될 때까지 진행되지 않도록 하라.
	- 출력 내용을 변경하여 수 일치가 되로록 하라.
		* 예)
		* Each person gets 2 pieces of pizza
		* Each person gets 1 piece of pizza
		* 남은 피자 조각도 위와 같이 수일치를 하여 출력되도록 하라.
	- 사람 수와 한 사람당 원하는 피자 조각 수를 입력 받은 다음, 피자를 몇 판 구매해야 하는지 계산하는 프로그램을 작성하라.

'''

numPeople = int(input("How many people? "))

numPizza = int(input("How many pizzas do you have? "))

numPiece = int(input("How many pieces are in a pizza? "))

print("{0} people with {1} pizzas".format(numPeople, numPizza))

print("Each person gets {0} pieces of pizza".format(numPizza * numPiece // numPeople))

print("There are {} leftover pieces.".format(numPizza * numPiece % numPeople))
