length = int(input("What is the length of the room in feet? "))

width = int(input("What is the width of the room in feet? "))

print("You entered dimensions of {0} feet by {1} feet".format(length, width))

square_feet = length * width
square_meters = square_feet * 0.092903

print("The area is {0} square feet {1} square meters".format(square_feet, square_meters))