def binary_search(data, n, target):
    low = 0
    high = n - 1
    while True:
        middle = (low + high) // 2
        if target == data[middle]:
            # print(data[middle])
            print('1')
            break
        elif target < data[middle]:
            # print(data[middle])
            high = middle - 1
        else:
            # print(data[middle])
            low = middle + 1
        if low > high:
            print('0')
            break


len, target = list(map(int, input().split()))
array = list(map(int, input().split()))
binary_search(array, len, target)
