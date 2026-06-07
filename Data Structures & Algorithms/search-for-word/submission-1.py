class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        def backtrack(x, y, i):
            if i == len(word):
                return True

            if x < 0 or x >= ROWS:
                return False
            if y < 0 or y >= COLS:
                return False
            if board[x][y] == "#" or board[x][y] != word[i]:
                return False

            board[x][y] = "#"
            
            wordFound = (
                backtrack(x+1, y, i+1) or 
                backtrack(x-1, y, i+1) or
                backtrack(x, y+1, i+1) or
                backtrack(x, y-1, i+1)
            )

            board[x][y] = word[i]
            return wordFound
        
        for x in range(ROWS):
            for y in range(COLS):
                if backtrack(x, y, 0):
                    return True
        
        return False
        