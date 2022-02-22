# 연습문제 31. 카르보넨 심박수

pulse = float(input("Resting Pulse: "))

inputAge = float(input("\rAge: "))

def karvonenHeartRate(age, restingHR, intensity):
	return ((220 - age - restingHR) * intensity) + restingHR

print("Intensity  | Rate    ")
print("-----------|---------")
for i in range(55, 100, 5):
	print("{}%        | {:.0f} bpm".format(i, karvonenHeartRate(inputAge, pulse, i / 100)))