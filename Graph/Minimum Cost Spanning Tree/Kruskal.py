# need to understand
from heapq import heapify, heappop # python 힙 연산 함수들

N = 7
parent = [i for i in range(N + 1)]
rank = [0] * (N + 1)
vertex = [(7, 1, 2),
          (5, 1, 4),
          (7, 2, 1),
          (8, 2, 3),
          (9, 2, 4),
          (7, 2, 5),
          (8, 3, 2),
          (5, 3, 5),
          (5, 4, 1),
          (9, 4, 2),
          (7, 4, 5),
          (6, 4, 6),
          (7, 5, 2),
          (5, 5, 3),
          (7, 5, 4),
          (8, 5, 6),
          (9, 5, 7),
          (6, 6, 4),
          (8, 6, 5),
          (11, 6, 7),
          (9, 7, 5),
          (11, 7, 6)]


def find(a):
    if parent[a] == a:
        return a
    p = find(parent[a])
    parent[a] = p
    return parent[a]


def union(e1, e2):
    a = find(e1)
    b = find(e2)
    if a == b:
        return
    if rank[a] > rank[b]:
        parent[b] = a
    elif rank[a] < rank[b]:
        parent[a] = b
    else:
        rank[b] += 1
        parent[a] = b


def kruskal(v):
    heapify(v)
    cost = 0
    mst = []
    while v:
        c, a, b = heappop(v)
        if parent[a] != parent[b]:
            union(a, b)
            cost += c
            mst.append((c, a, b))

    print(cost)
    print(mst)


kruskal(vertex)