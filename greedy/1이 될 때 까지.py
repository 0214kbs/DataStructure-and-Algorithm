# N이 1이 될 때까지의 최소 횟수 구하기
# 과정 1. N에서 1 빼기
# 과정 2. N에서 K로 나누기 (대신 나누어 떨어져야 함)
from random import randint
import time

start_time = time.time()

n,k = map(int,input().split())
cnt = 0
while True:
    if(n==1):
        break
    if(n%k==0) :
        n//=k
        cnt+=1
    else :
        n-=1
        cnt+=1

print(cnt)

end_time = time.time()

print("시간 :", end_time - start_time)