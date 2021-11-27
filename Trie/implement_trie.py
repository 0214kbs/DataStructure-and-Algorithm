class Node(object):
    def __init__(self, key, data = None):
        self.key = key #단어의 글자 하나를 담는 곳
        self.data = data #마지막 글자의 경우, 단어전체를 data필드에 저장, 아닌경우는 null
        self.children = {}


class Trie:
    def __init__(self):
        self.head = Node(None)  #key = None

    #trie에 문자열 삽입
    def insert(self, string):
        current_node = self.head #루트부터!

        for char in string:
            if char not in current_node.children: #알파벳이 자식에 존재하지 않으면
                current_node.children[char] = Node(char)
            current_node = current_node.children[char] #curr_node를 업데이트
        current_node.data = string #string의 마지막 글자 차례이면, 노드의 data필드에 string 문자열 전체 저장

    #stringdl trie에 존재하는지 여부
    def search(self, string):
        current_node = self.head #root 부터 시작

        for char in string:
            if char in current_node.children:   # 알파벳이 자식에 존재하면
                current_node = current_node.children[char]  #curr_node 업데이트
            else:
                return False #d없으면 False 반환

        #string의 마지막 글자일때, current_node에 data가 있다면, string이 trie안에 존재하는 것!
        if current_node.data:
            return True
        else:
            return False

    #주어진 prefix로 시작하는 단어들 찾기
    def starts_with(self, prefix):
        current_node = self.head # root 부터 시작
        words = []

        #trie에서 prefix를 찾고 prefix의 마지막 글자 노드를 subtrie로 설정
        for p in prefix: #prefix 알파켓 한글자씩 비교
            if p in current_node.children: # 해당 알파벳이 자식에 존재하면
                current_node = current_node.children[p] #current_node를 업데이트
            else:
                return None
        current_node = [current_node]
        next_node = []
        while True:
            for node in current_node:
                if node.data:
                    words.append(node.data)
                next_node.extend(list(node.children.values))
            if len(next_node) != 0:
                current_node = next_node
                next_node = []
            else:
                break
        return words


