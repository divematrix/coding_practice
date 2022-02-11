# 연습문제 07. 직사각형 방의 면적 Area of A Rectangular Room

length = int(input("What is the length of the room in feet? "))

width = int(input("What is the width of the room in feet? "))

print("You entered dimensions of {0} feet by {1} feet".format(length, width))

square_feet = length * width

constFromFeetToMeters = 0.09290304

square_meters = square_feet * constFromFeetToMeters

print("The area is {0} square feet {1:.3f} square meters".format(square_feet, square_meters))