class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = -1
        while s[i] == ' ':
            i-= 1
        count = 0
        while len(s) + i >= 0 and s[i] != ' ':
            i -= 1
            count += 1
        return count

        
        