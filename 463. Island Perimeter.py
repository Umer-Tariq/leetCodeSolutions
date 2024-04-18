class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0])
        perimeter = 0
        for i in range(row):
            for j in range(col):
                count = 0
                if grid[i][j] == 1:
                    if i + 1 < row:
                        if grid[i + 1][j] == 1:
                            count += 1
                    if i - 1 >= 0:
                        if grid[i - 1][j] == 1:
                            count += 1
                    if j + 1 < col:
                        if grid[i][j + 1] == 1:
                            count += 1
                    if j - 1 >= 0:
                        if grid[i][j - 1] == 1:
                            count += 1
                    perimeter += (4 - count)
        return perimeter
                


        
        