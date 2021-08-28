def d(n):
    cnt = 0
    for i in list(str(n)):
        cnt = cnt + int(i)
    return int(n) + cnt


cnt = 0
check = []
for i in range(1, 10001):
    n = d(i)
    check.append(n)

for i in range(1, 10001):
    if i in check:  #생성자
        pass
    else: #self number
        print(i)
        cnt = cnt+1
print(cnt)

