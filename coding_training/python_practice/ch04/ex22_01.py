# 연습문제 22. 숫자 비교
import sys

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 == num2:
	sys.exit("first number is equal to second number")
if num2 == num3:
	sys.exit("second number is equal to third number")
if num1 == num3:
	sys.exit("first number is equal to third number")

max_num = -sys.maxsize -1
if max_num < num1:
	max_num = num1
if max_num < num2:
	max_num = num2
if max_num < num3:
	max_num = num3

print("The largest number is {}".format(max_num))