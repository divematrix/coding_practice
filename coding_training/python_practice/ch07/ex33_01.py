# 연습문제 33. Magic 8 Ball

import random

answer = ['Yes', 'No', 'Maybe', 'Ask again later']

question = input("What`s your question? ")

print(answer[random.randint(0, len(answer)-1)])