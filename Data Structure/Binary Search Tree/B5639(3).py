# need to correct
# stack 이용
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
n = []

while True:
    try:
        n.append(int(input()))
    except:
        break

stack = []
stack2 = []

while True:
    i = 1
    if n[i] > n[0]:
        stack2.append(n[i])
    else:
        stack.append(n[i])
    i = i + 1

stack.sort()

while True:
    if len(stack) != 0:
        print(stack.pop())
    else:
        if len(stack2) != 0:
            print(stack2.pop())
