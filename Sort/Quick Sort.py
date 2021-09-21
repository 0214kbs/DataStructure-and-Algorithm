def Quick_Sort(arr):
    def sort(low, high):
        if high <= low:
            return
        idx_p = partition(low, high)
        sort(low, idx_p - 1)
        sort(idx_p, high)

    def partition(low, high):
        pivot = arr[(low + high) // 2]
        print(pivot)
        while low <= high:
            while arr[low] < pivot:
                low += 1
            while arr[high] > pivot:
                high -= 1
            if low <= high:
                arr[low], arr[high] = arr[high], arr[low]
                print(low, end=" ")
                print(high)
                low, high = low + 1, high - 1
                print(arr)
        return low

    return sort(0, len(arr) - 1)


array = [3, 7, 2, 5, 1, 4, 6]
Quick_Sort(array)
