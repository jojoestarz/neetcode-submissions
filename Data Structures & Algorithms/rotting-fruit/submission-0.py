class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = []
        time, fresh = 0, 0
        rows,cols =len(grid),len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                    print(fresh)
                if grid[r][c] == 2:
                    q.append([r,c])
        while q and fresh > 0:
            for i in range(len(q)):
               row,col = q.pop(0)
               for dr,dc in directions:
                r,c = dr+row,dc+col
                if (r < 0 or r ==len(grid) or c < 0 or c == len(grid[0]) or grid[r][c] != 1):
                    continue
                grid[r][c] = 2
                q.append([r,c])
                fresh -=1
            time +=1
        return time if fresh == 0 else -1