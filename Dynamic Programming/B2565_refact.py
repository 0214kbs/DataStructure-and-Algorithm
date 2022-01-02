import sys
input = sys.stdin.readline
n = int(input())
line = [list(map(int, input().split())) for _ in range(n)]

line = sorted(line, key=lambda x:x[1])

cnt = 0
TorF = True

for i in range(n-1):
    if not TorF:
        if line[i-1][0] > line[i+1][0]:
            cnt += 1
        else:
            TorF = True
    else:
        if line[i][0] > line[i + 1][0]:
            cnt += 1
            TorF = False
        else:
            TorF = True


print(cnt)