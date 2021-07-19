# 이중 반복문 사용

n,m = map(int,input().split())

res =0

for i in range(n):
    data = list(map(int,input().split()))
    min_val = 10001 # 모든 수는 10000이하라는 조건이 있기 때문에 불가능한 수로 설정
    for j in data:
        min_val = min(min_val,j)    #가장 작은 값 찾기
    res = max(res,min_val)

print(res)