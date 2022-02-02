numPeople = int(input("How many people? "))

numPizza = int(input("How many pizzas do you have? "))

numPiece = int(input("How many pieces are in a pizza? "))

print("{0} people with {1} pizzas".format(numPeople, numPizza))

print("Each person gets {0} pieces of pizza".format(numPizza * numPiece // numPeople))

print("There are {} leftover pieces.".format(numPizza * numPiece % numPeople))
