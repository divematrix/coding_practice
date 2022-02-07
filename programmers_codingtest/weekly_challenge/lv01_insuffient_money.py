# 코딩 테스트 연습 > 위클리 챌린지 > 부족한 금액 계산하기
# https://programmers.co.kr/learn/courses/30/lessons/82612

# 최초 제출 코드
def solution(price, money, count):
    return max(price * (count * (count + 1) / 2) - money, 0)

# 람다식으로 간략히
# solution = lambda price, money, count: max(0, price * count * (count + 1) / 2 - money)