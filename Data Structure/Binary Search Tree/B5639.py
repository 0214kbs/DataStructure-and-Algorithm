# need to understand
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def postOrder(n):
    length = len(n)

    if length <= 1:
        return n

    for i in range(1, length):
        if n[i] > n[0]:
            return postOrder(n[1:i]) + postOrder(n[i:]) + [n[0]]

    return postOrder(n[1:]) + [n[0]]


n = []
while True:
    try:
        n.append(int(input()))
    except:
        break

n = postOrder(n)
for i in n:
    print(i)
