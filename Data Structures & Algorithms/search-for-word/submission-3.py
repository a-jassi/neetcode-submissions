class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        
        def backtrack(x, y, matched):
            if matched == len(word):
                return True
            
            if x < 0 or x >= ROWS:
                return False
            if y < 0 or y >= COLS:
                return False
            if board[x][y] == '.' or board[x][y] != word[matched]:
                return False
            
            board[x][y] = '.'
            
            wordMatched = (
                backtrack(x + 1, y, matched + 1) or
                backtrack(x - 1, y, matched + 1) or
                backtrack(x, y + 1, matched + 1) or
                backtrack(x, y - 1, matched + 1)
            )

            board[x][y] = word[matched]
            return wordMatched
        
        for x in range(ROWS):
            for y in range(COLS):
                if backtrack(x, y, 0):
                    return True
        
        return False


            
