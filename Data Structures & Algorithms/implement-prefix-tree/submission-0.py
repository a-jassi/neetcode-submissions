class PrefixTree:

    def __init__(self):
        self.children = {}
        self.isEnd = False

    def insert(self, word: str) -> None:
        currNode = self
        for c in word:
            if c not in currNode.children:
                currNode.children[c] = PrefixTree()
            
            currNode = currNode.children[c]
        currNode.isEnd = True

    def search(self, word: str) -> bool:
        currNode = self
        for c in word:
            if c not in currNode.children:
                return False
            currNode = currNode.children[c]
        return currNode.isEnd

    def startsWith(self, prefix: str) -> bool:
        currNode = self
        for c in prefix:
            if c not in currNode.children:
                return False
            currNode = currNode.children[c]
        return True
        