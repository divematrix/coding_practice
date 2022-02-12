# 연습문제 18. 온도 변환 Temperature Conversion

choice = input("Press C to convert from Fahrenheit to Celsius.\nPress F to convert from Celsius to Fahrenheit.\nYour choice: ")

input_temperature= float(input("Please enter the temperature in Fahrenheit: "))

output_temperature = float()

if choice == 'c' or choice == 'C':
	output_temperature = (input_temperature - 32) * 5 / 9
	choice = 'Celsius'
elif choice == 'f' or choice == 'F':
	output_temperature = (input_temperature * 1.8) + 32
	choice = 'Fahrenheit'

print("The temperature in {} is {:.0f}.".format(choice, output_temperature))