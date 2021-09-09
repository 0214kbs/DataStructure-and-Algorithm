# Node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def init_tree():
    global root

    root = Node("a")
    root.left = Node("b")
    root.right = Node("c")

    node = root.left
    node.left = Node("d")
    node.right = Node("e")

    node = root.right
    node.left = Node("f")
    node.right = Node("g")
    

def PreOrder(node):
    if node is None:
        return
    print(node.data, end=' ')
    PreOrder(node.left)
    PreOrder(node.right)


def InOrder(node):
    if node is None:
        return
    InOrder(node.left)
    print(node.data, end=' ')
    InOrder(node.right)


def PostOrder(node):
    if node is None:
        return
    PostOrder(node.left)
    PostOrder(node.right)
    print(node.data, end=' ')


init_tree()
PreOrder(root)
print(" ")
InOrder(root)
print(" ")
PostOrder(root)