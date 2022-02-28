# 연습문제 37. 암호 생성기

def getPassword (length, special, numbers):
	import random
	abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	spc = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '`', '~', '[', ']', '{', '}', ':', ';', '\'', '\"', ',', '.', '<', '>', '?', '/', '\\']

	passlist = []
	passlist += random.sample(abc, length - numbers - special)
	passlist += random.sample(num, numbers)
	passlist += random.sample(spc, special)
	random.shuffle(passlist)

	result = ""

	for foo in passlist:
		result += foo
	
	return result

length = int(input("What`s the minimum length? "))

special = int(input("How many special characters? "))

numbers = int(input("How many numbers? "))

print("Your password is {}".format(getPassword(length, special, numbers)))