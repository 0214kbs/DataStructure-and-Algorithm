import sys
from collections import deque


def DSLR(n):
    D = n * 2 % 10000
    S = n - 1 if n != 0 else 9999
    L = n % 1000 * 10 + n // 1000
    R = n % 10 * 1000 + n // 10
    return [D, S, L, R]


def bfs():
    q = deque()
    q.append([A, ''])
    visited[A] = True
    while q:
        x, y = q.popleft()
        dslr = DSLR(x)
        if x == B:
            print(y)
        if not visited[dslr[0]]:
            visited[dslr[0]] = True
            q.append([dslr[0], y + 'D'])
        if not visited[dslr[1]]:
            visited[dslr[1]] = True
            q.append([dslr[1], y + 'S'])
        if not visited[dslr[2]]:
            visited[dslr[2]] = True
            q.append([dslr[2], y + 'L'])
        if not visited[dslr[3]]:
            visited[dslr[3]] = True
            q.append([dslr[3], y + 'R'])


input = sys.stdin.readline
T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    visited = [False] * 10000
    bfs()
