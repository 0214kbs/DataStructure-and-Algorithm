n, m, k = map(int,input().split())
data = list(map(int, input().split()))

data.sort()

temp = m//(k+1)
tmp = m%(k+1)
cnt = temp*k*data[n-1] + temp*data[n-2] + tmp*data[n-1]

print(cnt)