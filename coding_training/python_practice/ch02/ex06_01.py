# 연습문제 06. 퇴직 계산기

a = int(input("What is your current age? "))

b = int(input("At what age would you like to retire? "))

import datetime

current = datetime.datetime.now()

print("you have {} years left until you can retire. It`s {}, so you can retire in {}.".format(b-a, current.year, current.year + b - a))