# 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 하는데, 그 중에서 가장 높은 숫자의 카드를 뽑도록 설정

# solution
# 각 행마다 가장 작은 수를 찾은 뒤에 그 중에서 가장 큰 수

n,m = map(int,input().split())

res =0

for i in range(n):
    data = list(map(int,input().split())) #내가 알아서 m만큼 입력해야 함
    min_val = min(data)
    res = max(res,min_val)

print(res)