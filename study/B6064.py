import sys
from math import gcd


def lcm(m, n):
    return m * n // gcd(m, n)


# def calendar(M,N,x,y):
#     for k in range(1, maxK + 1):
#         val_x = k % M
#         val_y = k % N
#         if val_x == x and val_y == y:
#             return k
#     return -1


    # maxI = maxK//M
    # for i in range(maxI):
    #     k = x+M*i
    #     val_y = k%N
    #     if y == val_y:
    #         return k
    # return -1


input = sys.stdin.readline
T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    maxK = lcm(M, N)
    k = 0
    # print(calendar(M,N,x,y))
    for i in range(x, maxK+1,M):
        if (i-y)%N == 0:
            k = i
            break
    print(k) if k else print(-1)
