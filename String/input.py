import sys
input = sys.stdin.readline #string

# 1 2 3 4 5
arr = list(map(int, input().split())) # map: list안의 값을 "int"자료형으로 변환하여 map 객체로 만드는 함수
print(arr)

# 1 5 -> a b 자료형에 넣어 따로 사용
# 이렇게 선언하면 어떤 숫자를 넣음과 상관없이 파이썬에서 자동으로 변환해줌
# 속도가 더 빠름
a, b = map(int, input().split())
print(a,b)

