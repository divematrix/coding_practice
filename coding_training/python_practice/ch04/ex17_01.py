# 연습문제 17. 혈중 알코올 농도 계산기 BAC Calculator

alcohol = float(input("How many ounces of alcohol did you drink? "))

weight = float(input("What is your weight in pounds? "))

ratio = 0.73 if input("Is your gender male? y/n") == 'y' else 0.6

time = float(input("How many hours have you been drinking? "))

BAC = alcohol * 5.14 / weight * ratio - 0.015 * time

print("Your BAC is {}. It {} legal for you to drive.".format(BAC, 'is' if BAC < 0.08 else 'is not'))