import heapq

heap = []
heapq.heappush(heap, 50)
heapq.heappush(heap, 10)
heapq.heappush(heap, 20)
print(heap)

heap2 = [40, 30, 20]
heapq.heapify(heap2)
print(heap2)

#pop
print(heapq.heappop(heap))
print(heap)

#원소 가져오기
print(heap2[1])

#max_heap
heap3 = [1,3,5,7,9]
max_heap = []
for i in heap3:
    heapq.heappush(max_heap,(-i, i))
print(max_heap)
max_item = heapq.heappop(max_heap)[1]
print(max_item)

