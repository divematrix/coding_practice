# 연습문제 44. 제품 검색

import json

f = open('./coding_training/python_practice/ch08/items.json', 'r', encoding='utf-8')
items = json.load(f)['products']
f.close()

while True:
	search_item = input("What is the product name? ")
	search_check = False
	for i in items:
		if i['name'] == search_item:
			print("Name : {}".format(i['name']))
			print("Price : ${}".format(i['price']))
			print("Quantity on hand : {}".format(i['quantity']))
			search_check = True
	
	if not search_check:
		print("Sorry, that product was not found in our inventory")
	else:
		break
