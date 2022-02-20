# 연습문제 29. 잘못된 입력 처리

foo = ""

while not type(foo) == float or foo == 0.0:
	foo = input("What is the rate of return? ")
	
	if foo.isdecimal():
		foo = float(foo)
		if foo == 0.0:
			print("Sorry. That`s not a valid input.")	
	else:
		print("Sorry. That`s not a valid input.")


print("It will take {} years to double your initial investment.".format(72 / foo))