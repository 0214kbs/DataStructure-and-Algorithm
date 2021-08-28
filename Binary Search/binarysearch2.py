#binary search with recursion
def binary_search(data, target, low, high):
    if low > high:
        print('0')
    mid = (low+high)//2
    if data[mid] == target:
        print('find')
        print(data[mid])
    elif data[mid] > target:
        binary_search(data,target,low,mid-1)
        print(data[mid])
    else:
        binary_search(data,target,mid+1,high)
        print(data[mid])


len, target = list(map(int, input().split()))
array = list(map(int, input().split()))
binary_search(array, target, 0, len)

