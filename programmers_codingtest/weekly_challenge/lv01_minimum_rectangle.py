# 코딩 테스트 연습 > 위클리 챌린지 > 최소 직사각형
# https://programmers.co.kr/learn/courses/30/lessons/86491

# 최초 제출 코드
def solution(sizes):
    width = 0
    height = 0
    
    for size in sizes:
        if size[0] < size[1]:
            size[0], size[1] = size[1], size[0]
        if size[0] > width:
            width = size[0]
        if size[1] > height:
            height = size[1]
    
    return width * height

# 다른 사람이 쓴 코드를 람다식으로 간략히
# solution = lambda sizes: max(max(x) for x in sizes) * max(min(x) for x in sizes)