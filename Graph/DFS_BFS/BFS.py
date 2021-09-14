from collections import deque

graph = {0: [4],
         1: [2, 3],
         2: [1, 4],
         3: [1, 4, 5],
         4: [0, 2, 3],
         5: [3, 6, 7],
         6: [5],
         7: [5, 6, 8, 9],
         8: [7],
         9: [7]}

visited = [False] * len(graph)


def bfs(g):
    q = deque([g[0]])
    visited[0] = True
    print(0)
    while q:
        nxts = q.popleft()
        for nxt in nxts:
            if not visited[nxt]:
                print(nxt)
                visited[nxt] = True
                q.append(g[nxt])


bfs(graph)