# 큰 수의 법칙

# 첫 줄에 n,m,k "3 4 5"와 같이 입력 받고 공백으로 구분 (k <= m)
# 둘째 줄에 n개의 자연수가 주어지는 데 공백으로 구분한다.
# 큰 수의 법칙에 따라 출력

# 첫 줄 : 숫자를 입력받아 공백으로 구분 (n,m,k)
n, m, k = map(int, input().split())

# 둘째 줄 : 숫자를 입력받아 공백으로 구분하여 list에 저장
num_data = list(map(int,input().split()))

num_data.sort() #data 오름차순으로 정렬

res = 0

while True:
    for i in range(k):
        if m == 0:
            break
        res += num_data[n-1]
        m -= 1
    if m == 0:
        break
    res += num_data[n-2]
    m -= 1

print(res)
