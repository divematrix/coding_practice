# 연습문제 32. 숫자 맞추기 게임

import random

def inputInt(prStr, *args):
	while True:
		foo = input(prStr)
		if foo.isdecimal():
			if len(args):
				for i in args:
					if int(foo) == i:
						return int(foo)
				print("You have wrong input.\nInput integer in given value.")
			else:
				return int(foo)
		else:
			print("You have wrong input.\nInput integer value.")

def benchNum(bench, num):
	if bench > num:
		print("Too low. ", end="")
	if bench < num:
		print("Too high. ", end="")
	return True if bench == num else False

def playGuess(bench):
	count = 0
	while True:
		foo = inputInt("Guess again: " if count else "I have my number. What`s your guess? ")
		count += 1
		if benchNum(bench, foo):
			print("You got it in {} guesses!".format(count))
			return

print("Let`s play Guess the Number.")

while True:
	difficulty = inputInt("Pick a difficulty level (1, 2, or 3): ", 1, 2, 3)

	playGuess(random.randint(1, 10 ** difficulty))

	again = input("Play again? ")
	
	if again == 'n' or again == 'N':
		break

print("Goodbye!")