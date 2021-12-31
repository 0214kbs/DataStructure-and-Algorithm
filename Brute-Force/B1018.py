n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append(input())

count = []

for n_start in range(n-7):
    for m_start in range(m-7):
        startW = 0
        startB = 0
        for i in range(n_start, n_start+8):
            for j in range(m_start, m_start+8):
                if (i+j) % 2 == 0:
                    if board[i][j] != 'W':
                        startW += 1
                    if board[i][j] != 'B':
                        startB += 1
                else:
                    if board[i][j] != 'B':
                        startW += 1
                    if board[i][j] != 'W':
                        startB += 1
        count.append(min(startW, startB))
print(min(count))

