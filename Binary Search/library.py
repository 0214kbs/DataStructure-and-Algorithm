from bisect import bisect_right, bisect_left

arr = [1,2,3,4,5]
print(bisect_left(arr,3)) #2  : (0, 1, "2")
print(bisect_right(arr,3)) #3  : (     "3"  4  5)