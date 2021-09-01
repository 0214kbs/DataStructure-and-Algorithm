from collections import deque

n, m = map(int, input().split())
maps = []
for i in range(n):
    maps.append(list(map(int, list(input()))))

# 상(-1,0),하(1,0), 좌(0,-1), 우(0,1)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        for i in range(4):  # 상하좌우
            nx = x + dx[i]
            ny = y + dy[i]

            # nx,ny이 maps 안에 있을때
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                # maps[nx][ny] == 1 : 길인 곳
                maps[nx][ny] = maps[x][y] + 1
                q.append((nx, ny))
    return maps[n - 1][m - 1]


print(bfs(0, 0))
# print(maps)
