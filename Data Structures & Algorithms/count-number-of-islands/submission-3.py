class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(x, y):
            if x < 0 or x >= ROWS:
                return
            if y < 0 or y >= COLS:
                return
            if grid[x][y] != '1':
                return
            
            grid[x][y] = '0'

            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)
        
        res = 0
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    res += 1
                    dfs(r, c)
        
        return res