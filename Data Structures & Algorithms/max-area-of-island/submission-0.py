class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        x = [-1, 1, 0, 0]
        y = [0, 0, -1, 1]

        def valid(i, j):
            return 0 <= i < n and 0 <= j < m

        def dfs(i, j):
            grid[i][j] = 0
            area = 1                      # count this cell
            for k in range(4):
                r, c = i + x[k], j + y[k]
                if valid(r, c) and grid[r][c] == 1:
                    area += dfs(r, c)     # add the neighbor's island size
            return area

        best = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    best = max(best, dfs(i, j))   # keep the largest island
        return best