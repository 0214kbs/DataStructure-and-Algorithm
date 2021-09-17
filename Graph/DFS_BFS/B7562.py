from collections import deque
import sys
input = sys.stdin.readline

t = int(input())  # test개수

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]


def bfs(fx, fy, tx, ty):
    q = deque()
    q.append((fx, fy))
    maps[fx][fy] = 1

    while q:
        a, b = q.popleft()

        if a == tx and b == ty:
            print(maps[tx][ty] - 1)
            return

        for j in range(8):
            x = a + dx[j]
            y = b + dy[j]

            if 0 <= x < i and 0 <= y < i and maps[x][y] == 0:
                maps[x][y] = maps[a][b] + 1
                q.append((x, y))


for _ in range(t):
    i = int(input())  # 한변의 길이
    fx, fy = map(int, input().split())  # fx fy : from x, from y
    tx, ty = map(int, input().split())  # tx ty : to x, to y

    # maps = [[0] * i] * i
    maps = [[0] * i for j in range(i)]
    bfs(fx, fy, tx, ty)
    # print(maps)
