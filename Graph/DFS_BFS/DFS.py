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


def dfs(g, cur):
    if False not in visited:
        return
    if not visited[cur]:
        print(cur)
        visited[cur] = True
        for nxt in g[cur]:
            dfs(g, nxt)


dfs(graph, 0)
