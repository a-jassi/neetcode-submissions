class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = defaultdict(set)
        row = defaultdict(set)
        sqr = defaultdict(set)

        for x in range(9):
            for y in range(9):
                cur = board[x][y]
                if cur == '.':
                    continue

                if (cur in col[y]
                    or cur in row[x]
                    or cur in sqr[(x // 3, y // 3)]):
                    return False

                row[x].add(cur)
                col[y].add(cur)
                sqr[(x // 3, y // 3)].add(cur)
        
        return True


