# 연습문제 39. 레코드 정렬

foo = [{'First Name':'John', 'Last Name': 'Johnson', 'Position': 'Manager', 'Separation date': '2016-12-31'}, {'First Name':'Tou', 'Last Name': 'Xiong', 'Position': 'Software Engineer', 'Separation date': '2016-10-15'}, {'First Name':'Michaela', 'Last Name': 'Michaelson', 'Position': 'District Manager', 'Separation date': '2015-12-19'}, {'First Name':'Jake', 'Last Name': 'Jacobson', 'Position': 'Programmer', 'Separation date': ''}, {'First Name':'Jacquelyn', 'Last Name': 'Jackson', 'Position': 'DBA', 'Separation date': ''}, {'First Name':'Sally', 'Last Name': 'Weber', 'Position': 'Web Developer', 'Separation date': '2015-12-18'}]

for j in range(len(foo) - 1, 0, -1):
	for i in range(0, j):
		if foo[i]['Last Name'] > foo[i+1]['Last Name']:
			foo[i], foo[i+1] = foo[i+1], foo[i]

print("Name                | Position          | Separation Date")

print("--------------------|-------------------|--------------------")

for i in foo:
	name = i['First Name'] + " " + i['Last Name']
	print("{:<20}| {:<18}| {}".format(name, i['Position'], i['Separation date']))