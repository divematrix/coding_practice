# 연습문제 36. 통계 계산

time = []

while True:
	num = input("Enter a number: ")

	if num.isdecimal():
		time.append(int(num))

	if num == "done":
		break

for i in time:
	
