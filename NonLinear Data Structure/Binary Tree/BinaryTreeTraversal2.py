class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


tree = {}
tree['a'] = Node('a', 'b', 'c')
tree['b'] = Node('b', 'd', None)
tree['c'] = Node('c', None, None)
tree['d'] = Node('d', None, None)


def PreOrder(node):
    print(node.data, end=' ')
    if node.left is not None:
        PreOrder(tree[node.left])
    if node.right is not None:
        PreOrder(tree[node.right])


def InOrder(node):
    if node.left is not None:
        InOrder(tree[node.left])
    print(node.data, end=' ')
    if node.right is not None:
        InOrder((tree[node.right]))


def PostOrder(node):
    if node.left is not None:
        PostOrder(tree[node.left])
    if node.right is not None:
        PostOrder(tree[node.right])
    print(node.data, end=' ')


PreOrder(tree['a'])
print(" ")
InOrder(tree['a'])
print(" ")
PostOrder(tree['a'])
