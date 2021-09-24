from heapq import heappush, heappop

INF = int(1e9)
n = 6
s = 4
a = 5
b = 6
fares = [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]


def solution(n, s, a, b, fares):
    graph = [[] * n for _ in range(n + 1)]

    for x, y, z in fares:
        graph[x].append([y, z])
        graph[y].append([x, z])

    def dijkstra(start):
        heap = []
        heappush(heap, [0, start])
        dp = [INF] * (n + 1)
        dp[start] = 0
        while heap:
            w, now = heappop(heap)
            for n_n, wei in graph[now]:
                n_w = wei + w
                if n_w < dp[n_n]:
                    dp[n_n] = n_w
                    heappush(heap, [n_w, n_n])
        return dp

    s_d = dijkstra(s)  # 출발지에서의 거리

    # s->(1~6) + (1~6)->a + (1~6)->b
    # sum[1] = s->1 + 1->a + 1->b
    sum = [0 for i in range(n)]

    for i in range(1, n+1):
        i_d = dijkstra(i)
        sum[i - 1] = s_d[i] + i_d[a] + i_d[b]

    sum.sort()
    for i in range(n):
        if sum[i] != 0:
            answer = sum[i]
            break
    # answer = sum[0]
    return answer


print(solution(n, s, a, b, fares))
