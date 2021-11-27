import sys

input = sys.stdin.readline


class Node(object):
    def __init__(self, key, data=None):
        self.key = key  # 단어의 글자 하나를 담는 곳
        self.data = data  # 마지막 글자의 경우, 단어전체를 data필드에 저장, 아닌경우는 null
        self.children = {}


class Trie:
    def __init__(self):
        self.head = Node(None)  # key = None

    # trie에 문자열 삽입
    def insert(self, string):
        current_node = self.head  # 루트부터!

        for char in string:
            if char not in current_node.children:  # 알파벳이 자식에 존재하지 않으면
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]  # curr_node를 업데이트
        current_node.data = string  # string의 마지막 글자 차례이면, 노드의 data필드에 string 문자열 전체 저장

    def search_prefix(self, string):
        current_node = self.head

        for s in string:
            current_node = current_node.children[s]

        if current_node.children:
            return False
        else:
            return True


T = int(input())

for _ in range(T):
    trie = Trie()
    n = int(input())
    lst = []
    for _ in range(n):
        # string = str(input())
        string=input().rstrip()     #rstrip을 쓰는 이유??????????????
        lst.append(string)
        trie.insert(string)

    res = True
    print(lst)
    for l in lst:
        if not trie.search_prefix(l):
            res = False
            break
    if res:
        print("YES")
    else:
        print("NO")
