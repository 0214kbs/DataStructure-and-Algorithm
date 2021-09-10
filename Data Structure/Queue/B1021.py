from collections import deque

n, m = map(int, input().split())
data = list(map(int, input().split()))
cnt = 0

q=deque([])
for i in range(1, n + 1):
    q.append(i)

for d in data:
    while True:
        if d == q[0]:
            q.popleft()
            break
        else:
            if q.index(d) > len(q)//2:
                q.rotate(1)
                cnt += 1
            else:
                q.rotate(-1)
                cnt += 1

print(cnt)