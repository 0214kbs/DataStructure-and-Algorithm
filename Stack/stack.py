arr = [1, 2, 3, 4, 5]

#스택에서의 삽입
arr.append(6)
print(arr)

#스택에서의 삭제
temp = arr.pop()
print(temp)
print(arr)

#파이썬에서 제공하는 추가적인 연산들

# 해당원소 스택에서 제거
arr.remove(3)
print(arr)

arr = [2,3,1,5,4]
#스택 정렬
arr.sort()
print(arr)

arr = [2,2,4,6,2,1]
#해당 원소의 개수
print(arr.count(2))

arr = [2,3,1,5,4,6,1]
#해당 원소의 위치
print(arr.index(4))

#원하는 위치에 해당 원소 삽입
arr.insert(0, 8)
print(arr)