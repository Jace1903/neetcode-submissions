class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 
        n=len(grid)
        m=len(grid[0])
        res=0
        def valid(i,j)->bool:
            if i<0 or i>=n or j<0 or j>=m:
                return False
            return True
        x=[-1,1,0,0]
        y=[0,0,-1,1]
        def dfs(i,j):
            grid[i][j]="0"
            for k in range(4):
                row=i+x[k]
                col=j+y[k]
                if valid(row,col) and grid[row][col]=="1":
                    dfs(row,col)
        for i in range(n):
            for j in range(m):
                if grid[i][j]=="1":
                    dfs(i,j)
                    res+=1
        return res