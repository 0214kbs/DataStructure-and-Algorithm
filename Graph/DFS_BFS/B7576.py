from collections import deque
import sys

input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 0:
                maps[nx][ny] = maps[x][y] + 1
                q.append([nx, ny])


m, n = map(int, input().split())
maps = []
q = deque()
for i in range(n):
    maps.append(list(map(int, input().split())))
    for j in range(m):  #익은 토마토 저장
        if maps[i][j] == 1:
            q.append([i, j])

bfs()

res = 0
for i in maps:
    for j in i:
        if j == 0 :
            print(-1)
            exit(0)
    res = max(res,max(i))
print(res-1)
