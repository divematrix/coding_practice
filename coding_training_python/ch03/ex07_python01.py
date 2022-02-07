'''
# 연습문제 07. 직사각형 방의 면적
	글로벌 환경에서 일을 하다 보면 국제표준 단위와 피트/야드 단위로 정보를 나타내야 할 일이 생길 것이다. 물론 어느 시점에 도량형을 변환해야 가장 정확한 값을 구할 수 있는지도 알아야 할 것이다. 방의 면적을 계산하는 프로그램을 작성하라. 방의 길이와 폭을 피트 단위로 입력 받은 다음 제곱피트와 제곱미터로 면적을 나타내보자.

## 출력 예
	- What is the length of the room in feet? 15
	- What is the width of the room in feet? 20
	- You entered dimensions of 15 feet by 20 feet
	- The area is 300 square feet 27.871 square meters

## 제약 조건
	- 출력문과 계산 부분을 분리할 것
	- 상수를 사용하여 변환 상수를 저장할 것

## 도전 과제
	- 입력 값으로 숫자만 받을 수 있도록 프로그램을 수정해보자. 숫자가 입력될 때까지 진행되지 않도록 하라.
	- 입력 값이 피트 단위인지 미터 단위인지를 선택하는 새로운 버전을 만들어보자.
	- 이 프로그램을 GUI 버전으로 구현하여 입력 값이 변경되는 즉시 바로 결과가 업데이트되도록 하라.
'''

length = int(input("What is the length of the room in feet? "))

width = int(input("What is the width of the room in feet? "))

print("You entered dimensions of {0} feet by {1} feet".format(length, width))

square_feet = length * width
square_meters = square_feet * 0.092903

print("The area is {0} square feet {1} square meters".format(square_feet, square_meters))