'''
## 연습문제 02. 글자 수 세기
	문자열을 입력받은 다음 입력받은 문자열과 문자열의 글자 수를 출력하는 프로그램을 작성하라.

### 출력 예
	- What is the input string? Homer
	- Homer has 5 characters.

### 제약 조건
	- 출력 결과에는 입력 받은 문자열이 그대로 나타나도록 할 것
	- 출력을 위해 하나의 출력문을 사용할 것
	- 문자열의 길이를 구하기 위해 프로그래밍 언어에서 제공하는 내장 함수를 사용할 것

### 도전 과제
	- 사용자가 아무것도 입력하지 않은 채로 엔터 키를 치면 무엇이라도 입력하라는 메세지를 나타내보자
	- 이 프로그램을 GUI(그래픽 사용자 인터페이스) 버전으로 작성하여 글자를 입력할 때마다 글자 수가 바로 바로 업데이트되도록 하라. 만일 여러분이 사용하는 언어에 GUI 라이브러리가 없다면 HTML과 JavaScript를 사용하라.
'''

# 문자열 입력 받기
a = input("What is the input string? ")

# 입력 받은 문자열 글자 수 세기
b = len(a)

# 문자열 + 숫자 일때 문자열이 숫자로만 이루어져 있으면 문자열이 숫자로 형변환되어 숫자 덧셈 계산이 이루어짐

# 문자열 + 문자열 형태를 원하므로 글자수를 문자로 형변환 해줘야 한다
c = str(b)

# 문자열 concatenate 하여 출력
print(a + " has " + c + " characters.")