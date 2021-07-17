# 거스름돈
# 거슬러 줘야 할 돈이 N원일 때 거슬러 줘야할 동전의 최소 개수를 구하여라

n = int(input())
cnt = 0

coin_types =[500,100,50,10]

for coin in coin_types:
    cnt += (n//coin)
    n %= coin

print(cnt)

