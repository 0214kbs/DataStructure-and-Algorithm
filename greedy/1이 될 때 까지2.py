import time

start_time = time.time()
n,k = map(int,input().split())
cnt = 0

while True:
    # n == k로 나누어떨어지는 수 가 될 때 까지 1 빼기
    target = (n//k) *k
    cnt += (n-target)
    n = target
    if n<k :
        break
    cnt +=1
    n//=k

cnt += (n-1)
print(cnt)

end_time = time.time()

print("시간 :", end_time - start_time)