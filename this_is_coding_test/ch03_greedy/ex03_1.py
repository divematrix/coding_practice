# 예제 3-1. 거스름돈

# 거스름돈으로 사용할 500원, 100원, 50원, 10원 동전 무한히 존재 가정
# 거스름돈이 N원 일때 거슬러 줘야 할 동전의 최소 개수 (단, N은 항상 10의 배수)

remain = int(input("input Remains : "))

coins = [500, 100, 50, 10]

count = 0

for coin in coins:
	count += remain // coin
	remain %= coin

print(count)