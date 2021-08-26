def d(n):
    cnt = 0
    for i in list(str(n)):
        cnt = cnt + int(i)
    return int(n) + cnt


check = []
for i in range(1, 10001):
    n = d(i)
    check.append(n)

for i in range(1, 10001):
    if i in check:
        pass
    else:
        print(i)
