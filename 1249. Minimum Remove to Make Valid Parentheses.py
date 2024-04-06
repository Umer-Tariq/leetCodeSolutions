class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        i = 0
        while i < len(s):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if len(stack) == 0:
                    s = s[:i] + s[i + 1:]
                    i -= 1
                else:
                    stack.pop()
            i += 1
        if len(stack) > 0:
            st = set(stack)
            s2 = ""
            for i in range(len(s)):
                if i not in st:
                    s2 += s[i]
            return s2
        else:
            return s
        