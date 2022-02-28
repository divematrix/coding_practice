# 연습문제 36. 통계 계산

def sum(list):
	result = 0
	for i in list:
		result += i
	return result

def average(list):
	return sum(list) / len(list)

def deviation(list):
	result = []
	for i in list:
		result.append(i - average(list))
	return result

def variance(list):
	result = 0
	for i in deviation(list):
		result += i ** 2
	return result / len(list)

def stddev(list):
	return variance(list) ** (1/2)


time = []

while True:
	num = input("Enter a number: ")

	if num.isdecimal():
		time.append(int(num))

	if num == "done":
		break

print("Numbers : ", end="")

for i in time:
	print("{} ".format(i), end="")

print("")

print("The average is {}.".format(average(time)))

print("The minimum is {}.".format(min(time)))

print("The maximum is {}.".format(max(time)))

print("The standard deviation is {}.".format(stddev(time)))