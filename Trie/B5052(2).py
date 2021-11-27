# #not use trie

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    lst = []
    res = True
    n = int(input())
    for i in range(n):
        lst.append(input().strip())
    lst.sort()
    print(lst)
    for i in range(n - 1):
        if lst[i] == lst[i + 1][0:len(lst[i])]:
            res = False

    if res:
        print("YES")
    else:
        print("NO")