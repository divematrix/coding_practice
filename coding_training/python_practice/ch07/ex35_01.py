# 연습문제 35. 승자 선택

import random

participant = []

while True:
	name = input("Enter a name: ")
	if name:
		participant.append(name)
	else:
		break

print("The winner is... {}".format(participant[random.randint(0, len(participant) - 1)]))