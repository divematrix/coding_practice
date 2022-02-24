# 연습문제 34. 사원 명단 삭제

employee = ['John Smith', 'Jackie Jackson', 'Chris Jones', 'Amanda Cullen', 'Jeremy Goodwin']

def printArray(arr):
	print("There are {} employees:".format(len(arr)))

	for i in arr:
		print(i)

printArray(employee)

employee.remove(input("Enter an employee name to remove: "))

printArray(employee)