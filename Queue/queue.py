#python에서 queue에 관련된 기본적인 연산/라이브러리
from collections import deque

arr = [1,2,3,4,5]
q = deque(arr) #queue 자료형으로 저장됨
print(q)

q.append(6)
print(q)

tmp = q.popleft()
print(tmp)
print(q)