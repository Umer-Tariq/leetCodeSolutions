class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        max = 0
        count = 0
        for item in s:
            if item == '(':
                count +=1 
            elif item == ')':
                if count > max:
                    max = count
                count -= 1
        return max
        