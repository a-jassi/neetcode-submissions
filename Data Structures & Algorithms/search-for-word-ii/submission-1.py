class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
    
    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isEnd = True
    

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addWord(word)
        
        ROWS, COLS = len(board), len(board[0])
        res = set()
        
        def backtrack(x, y, curr, node):
            if node.isEnd:
                res.add(curr)
            
            if x < 0 or x >= ROWS:
                return
            if y < 0 or y >= COLS:
                return
            if board[x][y] == '#' or board[x][y] not in node.children:
                return
            
            letter = board[x][y]
            board[x][y] = '#'

            backtrack(x+1, y, curr + letter, node.children[letter])
            backtrack(x-1, y, curr + letter, node.children[letter])
            backtrack(x, y+1, curr + letter, node.children[letter])
            backtrack(x, y-1, curr + letter, node.children[letter])
        
            board[x][y] = letter
        
        for x in range(ROWS):
            for y in range(COLS):
                backtrack(x, y, "", root)
        return list(res)
