class Node:
    def __init__(self, item, next):
        self.item = item  # node의 값
        self.next = next  # 다음 node를 가리키는 포인터


class Stack:
    def __init__(self):
        self.last = None

    def push(self, item):  # 연결리스트에 요소를 추가하면서 가장 마지막 값을 next로 지정, 포인터인 last는 가장 마지막으로 이동
        self.last = Node(item, self.last)

    def pop(self):  # 가장 마지막 item을 끄집어 내고 last 포인터를 한칸 앞으로 이동(이전 값을 가리킴)
        item = self.last.item
        self.last = self.last.next
        return item


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
#print(stack)

for _ in range(3):
    print(stack.pop())
