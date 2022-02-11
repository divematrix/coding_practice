# 연습문제 05. 간단한 수학 Simple Math

str1 = input("What is the first number? ")

str2 = input("What is the second number? ")

n1 = int(str1)
n2 = int(str2)

print("{0} + {1} = {2}\n{0} - {1} = {3}\n{0} * {1} = {4}\n{0} / {1} = {5}".format(n1, n2, n1 + n2, n1 - n2, n1 * n2, n1 / n2))