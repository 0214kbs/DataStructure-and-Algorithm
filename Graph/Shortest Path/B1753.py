from heapq import heappush, heappop
import sys
from collections import defaultdict

input = sys.stdin.readline
graph = defaultdict(list)
V, E = map(int, input().split())  # V: 정점 개수 , E: 간선 개수
K = int(input())  # 시작 정점

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())  # u->v (w가중치)
    graph[u].append((v, w))


INF = int(1e9)
# distance = [INF] * (V + 1)
dp = [INF] * (V+1)

def dijkstra(start):
    heap = []
    heappush(heap, [0,start])
    # dp = [INF] * (V+1)
    dp[start] = 0
    while heap:
        w, now = heappop(heap)
        for n_n, wei in graph[now]:
            n_w = wei + w
            if n_w < dp[n_n]:
                dp[n_n] = n_w
                heappush(heap,[n_w,n_n])



dijkstra(K)

for i in range(1, V + 1):
    if dp[i] == INF:
        print("INF")
    else:
        print(dp[i])
