length = float(input("What is the length of the ceiling? "))

width = float(input("What is the width of the ceiling? "))

square = length * width

import math
need = math.ceil(square / (9 * 9))

print("You will need to purchase {0} liters of paint to cover {1} square meters.".format(need, square))