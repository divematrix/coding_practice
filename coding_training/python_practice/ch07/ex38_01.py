# 연습문제 38. 필터링 값

def toList(list):
	result = []
	for i in list:
		result.append(int(i))
	return result

def filterEvenNumbers(list):
	result = []
	for i in list:
		if i % 2 == 0:
			result.append(i)
	return result

inputList = input("Enter a list of numbers, separated by spaces : ").split()
inputList = toList(inputList)
inputList = filterEvenNumbers(inputList)

print("The even numbers are", end="")

for i in inputList:
	print(" {}".format(i), end="")