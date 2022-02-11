# 연습문제 15. 암호 검증 Password Verification

savedPassword = 'abc$123'

inputPassword = input("What is the password: ")

if savedPassword == inputPassword:
	print("Welcome!")
else:
	print("That password is incorrect.")