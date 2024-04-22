class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        st = set(deadends)

        que = []
        start = '0000'
        level = 0

        if start in st:
          return -1

        que.append(start)
        st.add(start)

        while que:
          n = len(que)
          while n:
            n -= 1
            curr = que.pop(0)
            if curr == target:
              return level
            for i in range(4):
              ch = curr[i]
              inc = None
              dec = None
              if ch == '0':
                dec = '9'
              else:
                dec = chr(ord(ch) - 1)

              if ch == '9':
                inc = '0'
              else:
                inc = chr(ord(ch) + 1)
              if i != 3:
                temp = curr[:i] + dec + curr[i+1:]
              else:
                temp = curr[:i] + dec
              if temp not in st:
                que.append(temp)
                st.add(temp)
              if i != 3:
                temp = curr[:i] + inc + curr[i+1:]
              else:
                temp = curr[:i] + inc
              if temp not in st:
                que.append(temp)
                st.add(temp)
          level += 1
        
        return -1
