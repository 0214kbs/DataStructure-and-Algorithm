#need to correct
def d(n):
    cnt = n
    while n != 0:
        cnt = cnt + int(n % 10)
        n = int(n / 10)
    return int(cnt)

cnt = 0
check = [False for i in range(10001)]
for i in range(1, 10001):
    n = d(i)
    if n < 10001:
        check[n]=True

for i in range(1, 10001):
    if not check[i]:
        print(i)
        cnt = cnt+1

print(cnt)
