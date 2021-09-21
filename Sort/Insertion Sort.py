def Insertion_Sort(arr):
    for end in range(1, len(arr)):
        for i in range(end, 0, -1):  # end부터 0까지 -1
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
            print(arr)


arr = [4, 2, 3, 6, 1, 5]
Insertion_Sort(arr)
