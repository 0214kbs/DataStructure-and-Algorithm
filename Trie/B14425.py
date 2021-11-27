import sys

input = sys.stdin.readline


class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        current_node = self.head

        for char in string:
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]
        current_node.data = string

    def search(self, string):
        current_node = self.head

        for char in string:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return False
        if current_node.data:
            return True
        else:
            return False


n, m = map(int, input().split())
trie = Trie()
cnt = 0

for i in range(n + m):
    # input을 그대로 사용하면 "TypeError 'builtin_function_or_method' object is not iterable" 에러 발생
    string = str(input())
    if i < n:
        trie.insert(string)
    else:
        if trie.search(string): #true
            cnt += 1
print(cnt)
