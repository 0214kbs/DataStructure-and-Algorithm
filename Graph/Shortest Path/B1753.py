from heapq import heappush, heappop
import sys
from collections import defaultdict

graph = defaultdict(list)
sys.setrecursionlimit(10 ** 6)
V, E = map(int, sys.stdin.readline().split())  # V: 정점 개수 , E: 간선 개수
K = int(input())  # 시작 정점
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())  # u->v (w가중치)
    graph[u].append((v, w))


# print(graph)


# dijkstra function 부분만 다시!
def dijkstra(graph):
    q = [(0, K)]  # 우선순위 큐 생성, (거리, 정점)
    distance = defaultdict(int)  # 거리 정보를 담을 dict 생성

    while q:
        dist, node = heappop(q)  # 거리, 정점 추출
        if node not in distance:  # 탐색하지 않은 node이면 탐색 진행
            distance[node] = dist  # 거리 정보 갱신
            for v, w in graph[node]:  # 인접 노드로 이동
                update = dist + w  # 거리 정보 갱신
                heappush(q, (update, v))  # 우선순위 큐에 삽입

    for i in range(1, V + 1):
        if i == K:  # 시작 정점은 거리 0 출력
            print('0')
        elif not distance[i]:  # 경로가 존재하지 않은 경우
            print('INF')
        else:  # 최단 경로가 존재하면
            print(distance[i])


dijkstra(graph)
