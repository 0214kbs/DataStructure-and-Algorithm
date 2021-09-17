from heapq import heapify, heappop, heappush
from collections import defaultdict

edge = [(7, 1, 2),
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

vertex = defaultdict(list)
for e in edge:
    c, a, b = e
    vertex[a].append((c, a, b))
    vertex[b].append((c, b, a))


def prim(v, r):
    visit = set([r])
    cost = 0
    mst = []
    heap = v[r]
    heapify(heap)

    while heap:
        c, a, b = heappop(heap)
        if b not in visit:
            visit.add(b)
            cost += c
            mst.append((c, a, b))

            for nxt in v[b]:
                if nxt[2] not in visit:
                    heappush(heap, nxt)
    print(cost)
    print(mst)


prim(vertex, 1)
