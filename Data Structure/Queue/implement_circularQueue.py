class circularQueue:
    def __init__(self, k: int):  # k: queue 크기
        self.q = [None] * k
        self.maxlen = k
        self.pFront = 0
        self.pRear = 0

    # enQueue(): rear pointer 이동
    def enQueue(self, value: int) -> bool:
        if self.q[self.pRear] is None:
            self.q[self.pRear] = value
            self.pRear = (self.pRear + 1) % self.maxlen
            return True
        else:
            return False

    # deQueue(): front pointer 이동
    def deQueue(self) -> bool:
        if self.q[self.pFront] is None:
            return False
        else:
            self.q[self.pFront] = None
            self.pFront = (self.pFront + 1) % self.maxlen
            return True

    def Front(self) -> int:
        return 1 if self.q[self.pFront] is None else self.q[self.pFront]

    def Rear(self) -> int:
        return -1 if self.q[self.pRear - 1] is None else self.q[self.pRear - 1]

    def isEmpty(self) -> bool:
        return self.pFront == self.pRear and self.q[self.pFront] is None

    def isFull(self) -> bool:
        return self.pFront == self.pRear and self.q[self.pFront] is not None


cQ = circularQueue(6)
cQ.enQueue(4)
cQ.enQueue(3)
cQ.enQueue(2)
cQ.enQueue(1)
print(cQ.Front())
cQ.deQueue()
print(cQ.Front())
print(cQ.Rear())
if cQ.isEmpty():
    print("empty")
else:
    print("not empty")
if cQ.isFull():
    print("full")
else:
    print("not full")
