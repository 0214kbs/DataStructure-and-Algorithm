import sys
input = sys.stdin.readline
n=int(input())
arr = list(map(int, input().split()))
res = [1] *n
for i in range(1,n):
    for j in range(i):
        if arr[j] < arr[i]:
            res[i] = max(res[i],res[j]+1)


print(max(res))