class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        fresh = [0]

        def addCell(r, c):
            if r < 0 or r >= ROWS:
                return
            if c < 0 or c >= COLS:
                return
            if grid[r][c] in [0, 2]:
                return
            grid[r][c] = 2
            fresh[0] -= 1
            q.append((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    fresh[0] += 1
        
        time = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            time += 1
        
        return max(0, time - 1) if fresh[0] == 0 else -1