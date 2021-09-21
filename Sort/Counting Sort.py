def counting_sorted(arr, K):
    c = [0] * K
    sorted_arr = [0] * len(arr)

    for i in arr:
        c[i] += 1

    for i in range(1, K):
        c[i] += c[i - 1]

    for i in range(len(arr)):
        sorted_arr[c[arr[i]] - 1] = arr[i]
        c[arr[i]] -= 1
        print(c)
    return sorted_arr


arr = [1,3,2,4]
print(counting_sorted(arr, 6))