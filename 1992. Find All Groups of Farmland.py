class Solution(object):
    def findFarmland(self, land):
        """
        :type land: List[List[int]]
        :rtype: List[List[int]]
        """

        def dfs(i, j, row, col, ans):
          land[i][j] = -1
          if (i - 1 < 0 or land[i - 1][j] == 0) and (j - 1 < 0 or land[i][j - 1] == 0):
            ans.append(i)
            ans.append(j)
          if (i + 1 >= row or land[i + 1][j] == 0) and (j + 1 >= col or land[i][j + 1] == 0):
            ans.append(i)
            ans.append(j)
            return ans
          if i + 1 < row:
            if land[i + 1][j] == 1:
               return dfs(i + 1, j, row, col, ans)
            
          if i - 1 > 0:
            if land[i - 1][j] == 1:
              return dfs(i - 1, j, row, col, ans)

          if j + 1 < col:
            if land[i][j + 1] == 1:
              return dfs(i, j + 1, row, col, ans)

          if j - 1 > 0:
            if land[i][j - 1] == 1:
              return dfs(i, j - 1, row, col, ans)



        row = len(land)
        col = len(land[0])
        final_ans = []
        for i in range(row):
          for j in range(col):
            if land[i][j] == 1:
              ans = dfs(i, j, row, col, [])
              final_ans.append(ans)
        final_ans = [inner_list for inner_list in final_ans if inner_list]
        return final_ans
