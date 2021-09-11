import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def find(a):
    if parent[a] == a:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]


def union(i, j):
    a = find(i)
    b = find(j)

    if a == b:
        return
    if a > b:
        parent[b] = a
    # elif a < b:
    else:
        parent[a] = b
    # else:
    #     b += 1
    #     parent[a] = b


n, m = map(int, input().split())
parent = [i for i in range(n)]
isprint = 0
for i in range(m):
    a, b = map(int, input().split())
    if find(a) == find(b):
        print(i + 1)
        isprint = 1
        break
    union(a, b)

if isprint == 0:
    print('0')
