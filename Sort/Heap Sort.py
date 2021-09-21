def Heap_Sort(arr):
    def heapify(i, l):
        largest = i
        left, right = i * 2 + 1, i * 2 + 2
        if left < l and arr[largest] < arr[left]:
            largest = left
        if right < l and arr[largest] < arr[right]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(largest, l)

    n = len(arr)

    for idx in range(n // 2 - 1, -1, -1):
        heapify(idx, n)
    for i in range(n - 1, 0, -1):
        heapify(0, i)  # 0부터 i-1까지 heapify

    return arr


arr = [3, 7, 2, 5, 1, 4, 6]
print(Heap_Sort(arr))
