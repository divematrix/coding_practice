# 연습문제 16. 합법적으로 운전 가능한 연령 Legal Drive Age

inputAge = int(input("What is your age? "))

judgeStr = ("You are " if inputAge >= 16 else "You are not ") + "enough to legally drive."

print(judgeStr)