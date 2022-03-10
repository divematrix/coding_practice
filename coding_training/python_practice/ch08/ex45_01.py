# 연습문제 45. 단어 탐색

f = open('./coding_training/python_practice/ch08/ex45_input.txt', 'r', encoding='utf-8')
lines = f.readlines()
f.close()

count = 0
result = []

for line in lines:
	if 'utilize' in line:
		count += 1
		line = line.replace('utilize', 'use')
	result.append(line)

output_file_name = input("input output file name : ")

f = open('./coding_training/python_practice/ch08/{}.txt'.format(output_file_name), 'w', encoding='utf-8')
f.writelines(result)
f.close()