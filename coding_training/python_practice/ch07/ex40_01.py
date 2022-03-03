# 연습문제 40. 필터링 레코드

foo = [{'First Name':'John', 'Last Name': 'Johnson', 'Position': 'Manager', 'Separation date': '2016-12-31'}, {'First Name':'Tou', 'Last Name': 'Xiong', 'Position': 'Software Engineer', 'Separation date': '2016-10-15'}, {'First Name':'Michaela', 'Last Name': 'Michaelson', 'Position': 'District Manager', 'Separation date': '2015-12-19'}, {'First Name':'Jake', 'Last Name': 'Jacobson', 'Position': 'Programmer', 'Separation date': ''}, {'First Name':'Jacquelyn', 'Last Name': 'Jackson', 'Position': 'DBA', 'Separation date': ''}, {'First Name':'Sally', 'Last Name': 'Weber', 'Position': 'Web Developer', 'Separation date': '2015-12-18'}]

srch = input("Enter a search string : ")

result = []

for i in foo:
	if srch in i['First Name']:
		result.append(i)
	elif srch in i['Last Name']:
		result.append(i)

print("\nResult : ")
print("Name                | Position          | Separation Date")
print("--------------------|-------------------|------------------")

for i in result:
	name = i['First Name'] + " " + i['Last Name']
	print("{:<20}| {:<17} | {}".format(name, i['Position'], i['Separation date']))