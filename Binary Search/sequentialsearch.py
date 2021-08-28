def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i + 1

input_data = input("생성할 원소 개수 입력한 다음 한 칸 띄고 찾을 문자열을 입력 : ").split()
n = int(input_data[0])
target = input_data[1]

arr = input("문자열 입력 : ").split()

print(sequential_search(n, target, arr))
