#need to correct
class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right


def PostOrder(node):
    if node.left is not None:
        PostOrder(tree[node.left])
    if node.right is not None:
        PostOrder(tree[node.right])
    print(node.data, end=' ')


tree = {}
n = []
while True:
    try:
        n.append(input())
    except:
        break

tree[n[0]] = Node(n[0], None, None)
for i in range(1, len(n)):
    # print(i)
    for j in range(0, i):
        # print(n[i])
        # print(n[j])
        if n[j] > n[i]:
            if tree[n[j]].left is None:
                tree[n[j]] = Node(n[j], n[i], None)
                tree[n[i]] = Node(n[i], None, None)
                break
            else:
                j = j + 1
        else:
            if tree[n[j]].right is None:
                tree[n[j]] = Node(n[j], None, n[i])
                tree[n[i]] = Node(n[i], None, None)
                break
            else:
                j = j + 1

PostOrder(tree[n[0]])
