# 연습문제 28. 숫자 추가

num_array = []

for i in range(0,5):
	num_array.append(float(input("Enter a number: ")))\

total = 0

for i in num_array:
	total += i

print("The total is {:.0f}".format(total))