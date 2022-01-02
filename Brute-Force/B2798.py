n,m= map(int, input().split())
cards = list(map(int, input().split()))
sum = []

for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if cards[i] + cards[j] + cards[k] > m:
                continue
            else:
                sum.append(cards[i]+cards[j]+cards[k])

print(max(sum))