# 연습문제 19. BMI 계산기 BMI Calculator

weight = float(input("How many kilograms do you weigh? "))
height = float(input("How tall are you in meters? "))

bmi = weight / (height * height)

health_guide = ""

if bmi < 18.5:
	health_guide += "underweight. You should see your doctor."
elif bmi >= 18.5 and bmi < 25:
	health_guide += "within the ideal weight range."
elif bmi >= 25:
	health_guide += "overweight. You should see your doctor."

print("Your BMI is {}\nYou are {}".format(bmi, health_guide))