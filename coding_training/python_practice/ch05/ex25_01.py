# 연습문제 25. 암호 길이 점검

password = input("password check : ")

state_dic = {1:'very weak', 2:'weak',
 3:'normal', 4:'strong', 5:'very strong'}

def passwordValidator(pw):
	if pw.isdecimal():
		return 3 if (len(pw) >= 8) else 1
	if pw.isalpha():
		return 3 if (len(pw) >= 8) else 2
	if pw.isalnum():
		return 4 if (len(pw) >= 8) else 3
	return 5 if (len(pw) >= 8) else 3

print("The password '{}' is a {} password.".format(password, state_dic[passwordValidator(password)]))