from collections import deque

n = int(input())
arr = []

for i in range(1,n+1):
    arr.append(i)

q = deque(arr)

while True:
    if len(q)==1:
        print(q[0])
        break
    q.popleft()
    top = q.popleft()
    q.append(top)
