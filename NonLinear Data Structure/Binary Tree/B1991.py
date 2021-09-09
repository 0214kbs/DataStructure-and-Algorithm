#need to correct
# Node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def PreOrder(node):
    if node == ".":
        return
    print(node.dat)
    PreOrder(node.left)
    PreOrder(node.right)


def InOrder(node):
    if node == ".":
        return
    InOrder(node.left)
    print(node.data)
    InOrder(node.right)


def PostOrder(node):
    if node == ".":
        return
    PostOrder(node.left)
    PostOrder(node.right)
    print(node.data)


global root

n = int(input())
for i in range(n):
    node, left, right = map(str,input().split())
    if i == 0:
        root = Node(node)
        root.left = Node(left)
        root.right = Node(right)
    else:
        while True:
            if node == root.left:
                node = root.left
                node.left = Node(left)
                node.right = Node(right)
                break
            elif node == root.right:
                node = root.right
                node.left = Node(left)
                node.right = Node(right)
                break

PreOrder(root)
print(" ")
InOrder(root)
print(" ")
PostOrder(root)