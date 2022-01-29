# 문자열 입력 받기
a = input("What is the input string? ")

# 입력 받은 문자열 글자 수 세기
b = len(a)

# 문자열 + 숫자 일때 문자열이 숫자로만 이루어져 있으면 문자열이 숫자로 형변환되어 숫자 덧셈 계산이 이루어짐

# 문자열 + 문자열 형태를 원하므로 글자수를 문자로 형변환 해줘야 한다
c = str(b)

# 문자열 concatenate 하여 출력
print(a + " has " + c + " characters.")