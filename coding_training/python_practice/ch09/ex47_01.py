# 연습문제 47. 우주에는 누가 있죠?

import requests
import json

# http://api.open-notify.org/astros.json

res = requests.get("http://api.open-notify.org/astros.json")

data = res.json() #dict 타입

data = data['people']

print("Name             | Craft")
print("-----------------|--------------")

for i in data:
	print("{:<17}| {:<14}".format(i['name'], i['craft']))
