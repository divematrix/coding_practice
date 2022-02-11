# 연습문제 08. 피자 파티 Pizza Party
	
people = int(input("How many people? "))

pizza = int(input("How many pizzas do you have? "))

piecePerPizza = int(input("How many pieces are in a pizza? "))

print("{0} people with {1} pizzas".format(people, pizza))

print("Each person gets {0} pieces of pizza".format(pizza * piecePerPizza // people))

print("There are {} leftover pieces.".format(pizza * piecePerPizza % people))
