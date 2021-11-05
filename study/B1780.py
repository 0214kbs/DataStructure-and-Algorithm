n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

ans = [0, 0, 0]


def find(right, down, num):
    check = paper[right][down]
    for i in range(right, right + num):
        for j in range(down, down + num):
            if paper[i][j] != check:
                for k in range(3):
                    for l in range(3):
                        find(right + k * (num // 3), down + l * (num // 3), num // 3)
                return
    if check == -1:
        ans[0] += 1
    elif check == 0:
        ans[1] += 1
    else:
        ans[2] += 1


find(0, 0, n)
print(ans[0])
print(ans[1])
print(ans[2])
