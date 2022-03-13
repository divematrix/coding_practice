# 연습문제 46. 단어 빈도 탐색

f = open('./coding_training/python_practice/ch08/ex46_input')
lines = f.readlines()
f.close()

words = []

for line in lines:
	line = line.split()
	for i in line:
		words.append(i)

words_set = set(words)

for word in words_set:
	count = 0

	for i in words:
		if word == i : count += 1
	
	stars = ""
	for i in range(count): stars += "*"

	print("{} : {}".format(word, stars))