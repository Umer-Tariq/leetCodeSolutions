class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        open = close = star = 0
        i = 0
        while i < len(s):
          if s[i] == '(':
            open += 1
          elif s[i] == '*':
            star += 1
          else:
            if open > 0:
              open -= 1
            elif star > 0:
              star -= 1
            else:
              return False
          i += 1
        star = 0
        j = len(s) - 1
        while j >= 0:
          if s[j] == ')':
             close += 1
          elif s[j] == '*':
             star += 1
          else:
            if close > 0:
              close -= 1
            elif star > 0:
              star -= 1
            else:
               return False
          j -= 1
        return True
        