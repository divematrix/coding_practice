# 연습문제 42. 데이터 파일 파싱

f = open('./coding_training/python_practice/ch08/name_list_input.csv', 'r')
lines = f.readlines()
f.close()

foo = []
for line in lines:
	a, b, c = line.split(', ')
	c = int(c.split()[0])
	foo.append({'Last':a, 'First':b, 'Salary':c})

print("{:<9}{:<9}{:<7}".format("Last", "First", "Salary"))
print("------------------------")
for i in foo:
	print("{:<9}{:<9}{:<7}".format(i['Last'], i['First'], i['Salary']))