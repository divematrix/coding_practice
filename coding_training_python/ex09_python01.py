'''
# 연습문제 09. 페인트 계산기
	가끔은 반올림 대신 올림을 해야 하는 경우도 있다. 천장을 칠하는 데 필요한 페인트 양을 구하는 프로그램을 작성하라. 길이와 폭을 입력 받은 다음, 1리터에 {9m}^2를 칠한다고 가정하여 계산하자. 그리고 천장을 칠하는 데 필요한 페인트 양을 정수로 표현해보자.

## 출력 예
	- You will need to purchase 2 liters of paint to cover 10 square meters.

	반드시 1리터짜리 통 단위로 페인트를 구매해야 한다. 그렇기 때문에 이 문제를 해결하기 위해서는 반드시 올림을 해야 한다.

## 제약 조건
	- 상수를 사용하여 변환 상수를 저장할 것
	- 반드시 올림을 해서 정수 단위로 구할 것

## 도전 과제
	- 입력 값으로 숫자만 받을 수 있도록 프로그램을 수정해보자. 숫자가 입력될 때까지 진행되지 않도록 하라.
	- 원 모양의 방도 계산할 수 있도록 하라.
	- ㄴ자 모양의 방도 계산할 수 있도록 하라.
	- 모바일 버전으로 프로그램을 작성하여 철물점에서 사용할 수 있도록 하라.
'''

length = float(input("What is the length of the ceiling? "))

width = float(input("What is the width of the ceiling? "))

square = length * width

import math
need = math.ceil(square / (9 * 9))

print("You will need to purchase {0} liters of paint to cover {1} square meters.".format(need, square))