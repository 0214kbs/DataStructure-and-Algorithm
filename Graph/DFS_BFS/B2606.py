n = int(input())
m = int(input())
maps = [[] * n for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    maps[a].append(b)
    maps[b].append(a)

visited = [0] * (n + 1)


def dfs(v):
    visited[v] = True
    for i in maps[v]:
        if not visited[i]:
            dfs(i)


dfs(1)
cnt = 0
# print(visited)
for i in range(n + 1):
    if visited[i] == True:
        cnt += 1
print(cnt - 1)
