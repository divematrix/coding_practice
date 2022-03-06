# 연습문제 41. 이름 정렬

f = open("./coding_training/python_practice/ch08/name_list_input.txt", 'r')
lines = f.readlines()
f.close()

for i in range(0, len(lines)):
	lines[i] = lines[i].strip()

for i in range(len(lines) - 2, 0, -1):
	for j in range(0, i):
		if lines[j] > lines[j+1]:
			lines[j], lines[j+1] = lines[j+1], lines[j]

f = open("./coding_training/python_practice/ch08/name_list_output.txt", 'w')

f.write("Total of {} names".format(len(lines))+"\n")
f.write("------------------"+"\n")
for line in lines:
	f.write(line+"\n")

f.close()