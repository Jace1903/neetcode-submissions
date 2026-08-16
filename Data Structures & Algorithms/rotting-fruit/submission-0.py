from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        n, m = len(grid), len(grid[0])
        fresh = 0
        time = 0
        q = deque()

        def valid(i, j):
            return 0 <= i < n and 0 <= j < m

        x = [-1, 1, 0, 0]
        y = [0, 0, 1, -1]

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        while q and fresh > 0:
            s = len(q)
            for _ in range(s):
                r, c = q.popleft()
                for k in range(4):
                    row, col = r + x[k], c + y[k]
                    if valid(row, col) and grid[row][col] == 1:
                        grid[row][col] = 2
                        fresh -= 1
                        q.append((row, col))
            time += 1

        return -1 if fresh > 0 else time

        