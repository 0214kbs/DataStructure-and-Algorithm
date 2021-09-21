def Merge_Sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    low_arr = Merge_Sort(arr[:mid])
    high_arr = Merge_Sort(arr[mid:])
    merged_arr = []
    l = h = 0
    print(low_arr)
    print(high_arr)
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            h += 1
        print(merged_arr)
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    print("__------------------------")
    print(merged_arr)
    print("-----------------------------")
    return merged_arr


arr = [3, 4, 2, 5, 1, 7, 6]
print(Merge_Sort(arr))
