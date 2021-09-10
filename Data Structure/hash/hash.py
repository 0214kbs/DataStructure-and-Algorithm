# hash table은 key:element 이루어진 쌍들이 저장된 list/array
# hash table의 각 칸은 bucket
# bucket에 추가적으로 원소를 넣을려고 할 때, 이미 bucket이 차 있어 더 들어가지 못하는 상태 : Overflow가 발생
# hash 자료구조에 있어서 가장 중요한 것은 overflow 처리

dic = {1: 2, 3: 5}
print(dic[1])
