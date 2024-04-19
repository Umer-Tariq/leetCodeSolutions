class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(i, j):
            grid[i][j] = '-1'
            if i + 1 < row:
                if grid[i + 1][j] == '1':
                    dfs(i + 1, j)
            if i - 1 >= 0:
                if grid[i - 1][j] == '1':
                    dfs(i - 1, j)
            if j + 1 < col:
                if grid[i][j + 1] == '1':
                    dfs(i, j + 1)
            if j - 1 >= 0:
                if grid[i][j - 1] == '1':
                    dfs(i, j - 1)


        row = len(grid)
        col = len(grid[0])
        count = 0
        for i in range(row):
            for j in range(col):
              if grid[i][j] == '1':
                  dfs(i, j)
                  count += 1

        return count 
